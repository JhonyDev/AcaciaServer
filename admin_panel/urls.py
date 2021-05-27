from django.urls import path
from .views import (load)
urlpatterns = [
    path('inflate/', load),
]
