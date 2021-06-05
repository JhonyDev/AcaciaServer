from django.urls import path

from .views import *

urlpatterns = [
    path('post_photo', api_post_photo),
    path('post_user', api_post_user),
    path('post_interests', api_post_interest),
    path('post_like_fav', api_post_like_fav),

    path('delete_interests', api_delete_interest),
    path('delete_photo', api_delete_photo),

    path('get_image', api_show_image),
    path('get_user_images', get_user_images),
    path('get_user_interests', get_interest),
    path('get_user', get_user),
    path('get_exp', api_get_exp),
]
