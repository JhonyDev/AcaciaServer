from django.conf.urls.static import static
from django.urls import path

from AcaciaServer import settings
from .views import *

urlpatterns = [
                  path('', MainView.as_view(), name='main-view'),
                  path('posts/<int:result>/', PostJsonListView.as_view(), name='posts-json-view'),
                  path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
                  path('dashboard/js/<int:result>/', AdminJson.as_view(), name='admin-json-view'),
                  path('dashboard/button_click/<result>/', ButtonClick.as_view(), name='button-click-view'),
                  path('dashboard/password/', PassView.as_view(), name='pass-view'),
                  path('dashboard/password/js/', PassJson.as_view(), name='pass-view-js'),
                  path('dashboard/password/new_pass/<result>', NewPass.as_view(), name='pass-view-js'),
                  path('XYZ/', NewPass.as_view(), name='pass-sad-js'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
