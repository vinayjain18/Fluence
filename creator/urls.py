from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.history, name='history'),
    path('download/<int:content_id>/', views.download_content, name='download_content'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
