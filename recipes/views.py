from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from dashboard.models import Dashboard
from notifications.models import Notification
from .models import Recipe, MadeRecipe, SavedRecipe

def recipe_detail(request, pk, slug):
    recipe = Recipe.objects.get(pk=pk)
    liked = False
    made = False
    saved_recipes = SavedRecipe.objects.filter(recipe = recipe).filter(user = request.user)
    made_recipes = MadeRecipe.objects.filter(recipe = recipe).filter(user = request.user)
    if saved_recipes:
        liked = True
    if made_recipes:
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
    saved_recipe = SavedRecipe.objects.filter(recipe = recipe).filter(user = request.user)
    if saved_recipe:
        saved_recipe.delete()
    else:
        SavedRecipe.objects.create(user = request.user, recipe = recipe)

    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))
    
def RecipeMade(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    made_recipe = MadeRecipe.objects.filter(recipe = recipe).filter(user = request.user)
    if made_recipe:
        made_recipe.delete()
    else:
        MadeRecipe.objects.create(user = request.user, recipe = recipe)
        # Replace this with a call to the badge awarding system. The badge system should then be responsible
        # for making the call to create the notification
        Notification.objects.create(user = request.user, name='Test Notification')

    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))