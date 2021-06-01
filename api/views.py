from urllib.parse import urlparse, parse_qs

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Photo, Interest
from .serializers import UserSerializer, PhotoSerializer, InterestSerializer


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
def api_post_interest(request):
    interest = Interest()
    serializer = InterestSerializer(interest, data=request.data)
    if serializer.is_valid():
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
    user = User.objects.filter(user_id=query)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def get_interest(request):
    query = str(request.GET.get('user_id'))
    interest = Interest.objects.filter(user_id=query)
    serializer = InterestSerializer(interest, many=True)
    return Response(serializer.data)


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


def api_show_image(request):
    query = str(request.GET.get('photo_id'))
    return render(request, 'api/index.html', context={"image": Photo.objects.get(photo_id=query)
                                                      })
