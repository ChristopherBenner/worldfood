from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', views.view_dashboard, name='dashboard'),
    path('saved-recipes/', views.view_saved_recipes, name='saved_recipes'),
    path('made-recipes/', views.view_made_recipes, name='made_recipes'),
    path('liked-recipes/', views.view_liked_recipes, name='liked_recipes'),
]