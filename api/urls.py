from django.urls import path

from .views import (api_show_image,
                    api_post_photo,
                    api_post_user,
                    get_user_images,
                    get_interest,
                    api_post_interest,
                    api_delete_interest,
                    api_delete_photo,
                    get_user)

urlpatterns = [
    path('post_photo', api_post_photo),
    path('post_user', api_post_user),
    path('post_interests', api_post_interest),

    path('delete_interests', api_delete_interest),
    path('delete_photo', api_delete_photo),

    path('get_image', api_show_image),
    path('get_user_images', get_user_images),
    path('get_user_interests', get_interest),
    path('get_user', get_user),
]
