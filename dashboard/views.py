from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Dashboard
from recipes.models import SavedRecipe
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