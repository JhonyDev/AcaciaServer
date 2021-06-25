from django.conf.urls.static import static
from django.urls import path

from AcaciaServer import settings
from .views import MainView, PostJsonListView, DashboardView, AdminJson

urlpatterns = [
                  path('', MainView.as_view(), name='main-view'),
                  path('posts/<int:result>/', PostJsonListView.as_view(), name='posts-json-view'),
                  path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
                  path('dashboard/js/<int:result>/', AdminJson.as_view(), name='admin-json-view'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
