from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Photo
from .serializers import UserSerializer, PhotoSerializer


@api_view(['POST', ])
def api_post_user(request):
    user = User()
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


def api_show_image(request):
    query = str(request.GET.get('photo_id'))
    return render(request, 'api/index.html', context={"image": Photo.objects.get(photo_id=query)
                                                      })
