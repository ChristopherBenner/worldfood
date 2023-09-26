from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.view_notifications, name='notifications'),
]