from django.urls import path
from rest_framework import routers

from .views import *
from .cron import run_cron

router = routers.DefaultRouter()
router.register(r'transaction', MpesaTransactionsViewSet)

urlpatterns = [
    path('post_photo', api_post_photo),
    path('post_user', api_post_user),
    path('post_interests', api_post_interest),
    path('post_like_fav', api_post_exp),
    path('post_report', api_post_report),

    path('delete_interests', api_delete_interest),
    path('delete_photo', api_delete_photo),

    path('get_image', api_show_image),
    path('get_user_images', get_user_images),
    path('get_user_interests', get_interest),
    path('get_user', get_user),
    path('get_exp', api_get_exp),

    path('run_cron', run_cron()),

    path('mpesa-stk-push/', MpesaSTKApiView.as_view(),
         name='mpesa_stk_push'),

    path('mpesa-stk-confirmation/', MpesaSTKConfirmationApiView.as_view(),
         name='mpesa_stk_confirmation'),
]

urlpatterns += router.urls
