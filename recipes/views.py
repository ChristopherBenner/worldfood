from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from dashboard.models import Dashboard
from notifications.models import Notification
from .models import Recipe, MadeRecipe, SavedRecipe
from badges.functions import add_badge
def recipe_detail(request, pk, slug):
    recipe = Recipe.objects.get(pk=pk)
    liked = False
    made = False
    # Check to see if the user is logged in
    # If so, give the option for saved recipes and made recipes
    # Otherwise, prompt the user to log in before giving these options
    # Without the login check, an error shows which doesn't allow the recipe to be shown at all
    

    if request.user.is_authenticated: 
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
        # Notification.objects.create(user = request.user, description='Test Notification')
        # Badge.
        points = MadeRecipe.objects.filter(user = request.user).count()
        add_badge(request.user, 'Recipes Created', points)

    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))