from urllib.parse import urlparse, parse_qs

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Photo, Interest, Liked
from .serializers import UserSerializer, PhotoSerializer, LikedSerializer, InterestSerializer


@api_view(['POST', ])
def api_post_user(request):
    query = str(request.GET.get('user_id'))
    user = User()
    users = User.objects.filter(user_id=query)
    if users:
        print('-------------------')
        print('Users with id ' + query + ' Deleted')
        print('-------------------')
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
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    serializer = PhotoSerializer(photo, data=request.data)
    # user_id = body.get('user_id')
    # photo_url = body['photo_url']
    # list_photos = Photo.objects.filter(user_id=user_id, photo_url=photo_url)

    if serializer.is_valid():
        # if list_photos:
        #     return Response(serializer.data, status=status.HTTP_409_CONFLICT)
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
def api_post_like_fav(request):
    like_fav = Liked()
    serializer = LikedSerializer(like_fav, data=request.data)

    if serializer.is_valid():
        who = serializer.validated_data['who_liked']
        whom = serializer.validated_data['whom_liked']

        print('-----*********//////////*******------------')
        print(whom)
        print(who)

        likes = Liked.objects.filter(who_liked=who, whom_liked=whom)
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
def get_user_liked(request):
    query = str(request.GET.get('user_id'))
    liked = Liked.objects.filter(who_liked=query)
    serializer = LikedSerializer(liked, many=True)
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

    if whom == '*':
        liked = Liked.objects.filter(who_liked=who, like_fav=exp)
    elif who == '*':
        liked = Liked.objects.filter(whom_liked=whom, like_fav=exp)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    serializer = LikedSerializer(liked, many=True)

    return Response(serializer.data)


def api_show_image(request):
    query = str(request.GET.get('photo_id'))
    return render(request, 'api/index.html', context={"image": Photo.objects.get(photo_id=query)
                                                      })
