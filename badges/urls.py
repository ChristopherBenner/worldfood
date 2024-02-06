from django.urls import path
from . import views
app_name = 'badges'

urlpatterns = [
    path('', views.view_badges, name='badges'),
    path('<int:recipe_id>/<int:badge_id>/', views.badge_displayed, name='badge_displayed'),
]