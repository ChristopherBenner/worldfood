from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', views.view_dashboard, name='dashboard'),
    path('saved-recipes/', views.view_saved_recipes, name='saved_recipes'),
]