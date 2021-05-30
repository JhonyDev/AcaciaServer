from django.urls import path

from .views import (api_show_image,
                    api_post_photo,
                    api_post_user,
                    get_user_images)

urlpatterns = [
    path('post_photo', api_post_photo),
    path('post_user', api_post_user),
    path('get_image', api_show_image),
    path('get_user_images', get_user_images),
]
