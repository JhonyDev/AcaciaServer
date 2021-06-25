from django.conf.urls.static import static
from django.urls import path

from AcaciaServer import settings
from .views import MainView, PostJsonListView

urlpatterns = [
                  path('', MainView.as_view(), name='main-view'),
                  path('posts/', PostJsonListView.as_view(), name='posts-json-view'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
