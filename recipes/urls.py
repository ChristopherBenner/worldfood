# recipes/urls.py
from django.urls import path

from . import views
app_name = 'recipes'

urlpatterns = [
    path('<int:pk>/', views.get_redirect_url, name='recipe_redirect'),
    path('<int:pk>/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipe-save/<int:pk>/', views.RecipeSave, name='recipe_save'),
    path('recipe-made/<int:pk>/', views.RecipeMade, name='recipe_made'),
    path('recipe_liked/<int:pk>/', views.RecipeLiked, name='recipe_liked')
]