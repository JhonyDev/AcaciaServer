import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse, parse_qs
from base64 import b64encode

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import filters as filterz

from admin_panel.models import ReportedAccounts
from .models import User, Photo, Interest, Expression, MpesaTransaction
from .serializers import UserSerializer, PhotoSerializer, LikedSerializer, InterestSerializer, ReportSerializer, \
    MpesaTransactionSerializer


@api_view(['POST', ])
def api_post_user(request):
    query = str(request.GET.get('user_id'))
    user = User()
    users = User.objects.filter(user_id=query)
    if users:
        for user in users:
            user.delete()
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_post_report(request):
    query = str(request.GET.get('user_email'))
    report = ReportedAccounts()

    print('Query :: ' + query)

    reported_accounts = ReportedAccounts.objects.filter(user_email=query)
    if reported_accounts:
        for account in reported_accounts:
            account.delete()

    serializer = ReportSerializer(report, data=request.data)

    print()

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@csrf_exempt
def api_post_photo(request):
    photo = Photo()
    request.build_absolute_uri()
    url = request.get_full_path()
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    is_ver = query.get('is_verification')[0]
    user_id = query.get('user_id')[0]

    if is_ver == 'true':
        users = User.objects.filter(user_id=user_id)
        for user in users:
            user.verification_status = 'Verified'
            user.save()
            break

        photos = Photo.objects.filter(user_id=user_id, is_id='True')
        for photo in photos:
            photo.delete()

        expressions = Expression.objects.filter(who_liked=user_id)
        for expression in expressions:
            expression.ver_status = 'Verified'
            expression.save()

    serializer = PhotoSerializer(photo, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_post_interest(request):
    request.build_absolute_uri()
    url = request.get_full_path()
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    user_id = query.get('user_id')[0]
    head = query.get('head')[0]

    interest = Interest()
    if head == 'true':

        interests = Interest.objects.filter(user_id=user_id)
        for interest in interests:
            interest.delete()

    serializer = InterestSerializer(interest, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_post_exp(request):
    like_fav = Expression()
    serializer = LikedSerializer(like_fav, data=request.data)

    if serializer.is_valid():
        who = serializer.validated_data['who_liked']
        whom = serializer.validated_data['whom_liked']

        likes = Expression.objects.filter(who_liked=who, whom_liked=whom)
        for like in likes:
            like.delete()

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_interest(request):
    request.build_absolute_uri()
    url = request.get_full_path()
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    user_id = query.get('user_id')[0]
    interest = query.get('interest')[0]

    interests = Interest.objects.filter(user_id=user_id, interest=interest)
    for any_interest in interests:
        any_interest.delete()

    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE', ])
def api_delete_photo(request):
    request.build_absolute_uri()
    url = request.get_full_path()
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    user_id = query.get('user_id')[0]
    picture = query.get('picture')[0]

    picture.replace('http://192.168.1.107:8000', '')

    photos = Photo.objects.filter(user_id=user_id, picture=picture)
    for photo in photos:
        photo.delete()

    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET', ])
def get_user_images(request):
    query = str(request.GET.get('user_id'))
    photos = Photo.objects.filter(user_id=query)
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def get_user(request):
    users = User.objects.all()
    for target_user in users:
        transaction_list = MpesaTransaction.objects.filter(user_id=target_user.user_id)
        for transaction in transaction_list:
            if transaction.completed:
                target_user.paid_fee = True
                target_user.save()
                break

    query = str(request.GET.get('user_id'))
    if query == '*':
        user = User.objects.all()
    else:
        user = User.objects.filter(user_id=query)
        transaction_list = MpesaTransaction.objects.filter(user_id=query)
        for transaction in transaction_list:
            if transaction.completed:
                user.paid_fee = True
                break

    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def get_id(request):
    query = str(request.GET.get('user_email'))
    users = User.objects.filter(user_email=query)

    if users:
        for user in users:
            user.paid_fee = True
            user.save()
        response = Response({'detail': 'Given Access'},
                            status=status.HTTP_200_OK)
    else:
        users = User.objects.all()
        for user in users:
            transaction_list = MpesaTransaction.objects.filter(user_id=user.user_id)
            for transaction in transaction_list:
                if transaction.completed:
                    user.paid_fee = True
                    user.save()
                    break
        response = Response({'detail': 'Email not Not Found'},
                            status=status.HTTP_404_NOT_FOUND)

    return response


@api_view(['GET', ])
def get_interest(request):
    query = str(request.GET.get('user_id'))
    interest = Interest.objects.filter(user_id=query)
    serializer = InterestSerializer(interest, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def api_get_exp(request):
    request.build_absolute_uri()
    url = request.get_full_path()
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    who = query.get('who')[0]
    exp = query.get('exp')[0]
    whom = query.get('whom')[0]

    if who == '*' and exp == '*' and whom == '*':
        liked = Expression.objects.all()
    elif who == '*' and exp == '*' and whom != '*':
        liked = Expression.objects.filter(whom_liked=whom)
    elif who == '*' and exp != '*' and whom == '*':
        liked = Expression.objects.filter(exp=exp)
    elif who == '*' and exp != '*' and whom != '*':
        liked = Expression.objects.filter(exp=exp, whom_liked=whom)
    elif who != '*' and exp == '*' and whom == '*':
        liked = Expression.objects.filter(who_liked=who)
    elif who != '*' and exp == '*' and whom != '*':
        liked = Expression.objects.filter(who_liked=who, whom_liked=whom)
    elif who != '*' and exp != '*' and whom == '*':
        liked = Expression.objects.filter(who_liked=who, exp=exp)
    elif who != '*' and exp != '*' and whom != '*':
        liked = Expression.objects.filter(who_liked=who, whom_liked=whom, exp=exp)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    serializer = LikedSerializer(liked, many=True)

    return Response(serializer.data)


def api_show_image(request):
    query = str(request.GET.get('photo_id'))
    return render(request, 'api/index.html', context={"image": Photo.objects.get(photo_id=query)})


consumer_k = settings.CONSUMER_KEY
consumer_s = settings.CONSUMER_SECRET
pass_key = settings.PASSKEY
s_code = settings.SHORT_CODE
c_url = settings.CALLBACK_URL


class MpesaSTKApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, **kwargs):
        data = request.data

        if "user_id" and "user_phone" in data.keys():
            try:
                user = User.objects.get(
                    user_id=data["user_id"])
            except User.DoesNotExist:
                user = None

            if not user:
                return Response({'detail': 'Customer with that id does not exist, please confirm.'},
                                status=status.HTTP_404_NOT_FOUND)

            if "purpose" in data.keys():
                stk_purpose = data["purpose"]
            else:
                stk_purpose = "Subscription"

            if "amount" in data.keys():
                amount = data["amount"]
            else:
                amount = 2000
            Passkey = pass_key

            Shortcode = s_code
            callback_url = c_url

            def get_stk_token():
                consumer_key = consumer_k
                consumer_secret = consumer_s
                auth_url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
                r = requests.get(auth_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
                access_token = r.json()['access_token']
                return access_token

            access_token = get_stk_token()

            def get_time():
                now = str(datetime.now().strftime("%Y%m%d"))
                time = str(datetime.now().strftime("%H%M%S"))
                real = str(now + time)
                return real

            time_now = get_time()

            def encoded_pass():
                pwd = (str(Shortcode) + Passkey + time_now).encode('utf-8')
                pwd_enc = b64encode(pwd).decode('ascii')
                return pwd_enc

            pass_enc = encoded_pass()

            api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}

            request = {
                "BusinessShortCode": Shortcode,
                "Password": pass_enc,
                "Timestamp": time_now,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": data["user_phone"],
                "PartyB": Shortcode,
                "PhoneNumber": data["user_phone"],
                "CallBackURL": callback_url,
                "AccountReference": "4075259",
                "TransactionDesc": stk_purpose
            }

            response = requests.post(api_url, json=request, headers=headers)
            print(response.json())
            if response.status_code == 200:
                MpesaTransaction.objects.create(
                    user_id=data["user_id"],
                    user_phone=data["user_phone"],
                    purpose=stk_purpose,
                    amount=amount,
                    timestamp=time_now,
                    request_id=response.json()["MerchantRequestID"],

                )

            return Response({"detail": "Stk push Succesfull"}, status=status.HTTP_200_OK)

        else:
            return Response({"detail": "You need to pass the user phone number to make the stk push."},
                            status=status.HTTP_406_NOT_ACCEPTABLE)


class MpesaSTKConfirmationApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, **kwargs):
        data = request.data
        if data["Body"]["stkCallback"]["ResultCode"] == 0:
            try:
                transaction = MpesaTransaction.objects.get(
                    request_id=data["Body"]["stkCallback"]["MerchantRequestID"])
            except MpesaTransaction.DoesNotExist:
                transaction = None

            if transaction:
                transaction.completed = True
                transaction.save()
            user_id = transaction.user_id
            user = User.objects.get(user_id=user_id)
            user.paid_fee = True
            user.save()
        return Response({"detail": "Done"}, status=status.HTTP_200_OK)


class MpesaTransactionsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MpesaTransactionSerializer
    queryset = MpesaTransaction.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filterz.SearchFilter)
    filterset_fields = ('user_id', 'user_phone', 'completed', 'purpose')
    search_fields = ['user_id', 'user_phone', 'purpose']
