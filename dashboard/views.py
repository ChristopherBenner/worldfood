from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Dashboard
from recipes.models import SavedRecipe, MadeRecipe
from likes.models import Like
# Create your views here.
@login_required
def view_dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def view_saved_recipes(request):
    user = request.user
    saved_recipes = SavedRecipe.objects.filter(user = user)
    return render(request, 'dashboard/saved_recipes.html', {
        'saved_recipes': saved_recipes,
        'user': user,
    })

def view_made_recipes(request):
    user = request.user
    made_recipes = MadeRecipe.objects.filter(user = user)
    return render(request, 'dashboard/made_recipes.html', {
        'made_recipes': made_recipes,
    })

def view_liked_recipes(request):
    user = request.user 
    liked_recipes = Like.objects.filter(user = user)
    return render(request, 'dashboard/liked_recipes.html', {
        'liked_recipes': liked_recipes,
    })