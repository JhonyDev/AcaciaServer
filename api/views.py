from urllib.parse import urlparse, parse_qs

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Photo, Interest, Expression
from .serializers import UserSerializer, PhotoSerializer, LikedSerializer, InterestSerializer


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
    query = str(request.GET.get('user_id'))
    if query == '*':
        user = User.objects.all()
    else:
        user = User.objects.filter(user_id=query)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


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
