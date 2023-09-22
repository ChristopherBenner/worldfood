from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from dashboard.models import Dashboard
from .models import Recipe

def recipe_detail(request, pk, slug):
    recipe = Recipe.objects.get(pk=pk)
    liked = False
    made = False
    saved_recipes = Recipe.objects.filter(saved_recipes__username = request.user.username)
    made_recipes = Recipe.objects.filter(made_recipes__username = request.user.username)
    if recipe in saved_recipes:
        liked = True
    if recipe in made_recipes:
        made = True
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'liked': liked,
        'made': made,
    })

def get_redirect_url(request, pk):
    # need to write the appropriate test for this
    recipe = Recipe.objects.get(pk=pk)
    slug = recipe.slug
    return redirect(reverse('recipes:recipe_detail', args=(pk, slug)))

def RecipeSave(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    if recipe.saved_recipes.filter(id=request.user.id).exists():
        recipe.saved_recipes.remove(request.user)
    else:
        recipe.saved_recipes.add(request.user)

    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))
    
def RecipeMade(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    if recipe.made_recipes.filter(id=request.user.id).exists():
        recipe.made_recipes.remove(request.user)
    else:
        recipe.made_recipes.add(request.user)

    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))