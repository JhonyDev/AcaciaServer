from django.conf.urls.static import static
from django.urls import path

from AcaciaServer import settings
from .views import (load)

urlpatterns = [
                  path('', load),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
