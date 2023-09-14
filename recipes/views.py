from django.shortcuts import render
from .models import Recipe
# Create your views here.
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
    })