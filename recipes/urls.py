# recipes/urls.py
from django.urls import path

from . import views
app_name = 'recipes'

urlpatterns = [
    path('<int:pk>/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]