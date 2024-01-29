# countries/urls.py
from django.urls import path

from . import views
app_name = 'countries'

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('<int:pk>/', views.get_redirect_url, name='country_redirect'),
    path('<int:pk>/<slug:slug>/', views.recipe_list, name="recipe_list")
]