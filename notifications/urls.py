from django.urls import path
from . import views


app_name = 'notifications'

urlpatterns = [
    path('', views.view_notifications, name='notifications'),
    path('clear/', views.notifications_clear, name='notifications_clear'),
    path('notification-read/<int:pk>/', views.notification_read, name='notification_read'),
    path('api/', views.notification_list, name="notification_list"),
]