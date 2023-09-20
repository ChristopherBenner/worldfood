# recipes/urls.py
from django.urls import path

from . import views
app_name = 'recipes'

urlpatterns = [
    path('<int:pk>/', views.get_redirect_url, name='recipe_redirect'),
    path('<int:pk>/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipe-save/<int:pk>/', views.RecipeSave, name='recipe_save'),
]