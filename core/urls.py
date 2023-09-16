# core/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm
app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LoginForm), name='login'),
    path('signup/', views.signup_view, name='signup'),
]