from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from dashboard.models import Dashboard
from notifications.models import Notification
from .models import Recipe, MadeRecipe, SavedRecipe
from badges.functions import add_badge
from likes.models import Like
import requests, json

def recipe_detail(request, pk, slug):
    recipe = Recipe.objects.get(pk=pk)
    saved = False
    made = False
    liked = False
    # Check to see if the user is logged in
    # If so, give the option for saved recipes and made recipes
    # Otherwise, prompt the user to log in before giving these options
    # Without the login check, an error shows which doesn't allow the recipe to be shown at all
    

    if request.user.is_authenticated: 
        saved_recipes = SavedRecipe.objects.filter(recipe = recipe).filter(user = request.user)
        made_recipes = MadeRecipe.objects.filter(recipe = recipe).filter(user = request.user)        
        liked_recipes = Like.objects.filter(recipe = recipe).filter(user = request.user)
        
        if saved_recipes:
            saved = True
        if made_recipes:
            made = True
        if liked_recipes:
            liked = True
    
    """url = "https://yummly2.p.rapidapi.com/feeds/"
    #querystring = {"q":"/recipe/Stuffed-Onions-From-Afghanistan-9268792"}

    # The API Key should be moved into a separate file, and not included in the main files
    headers = {"X-RapidAPI-Key": "395ac24211msh69d8d498a22b082p1bf25djsn81214c5dc50b",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # Uncomment the lines below to access the api -> Not used during testing
    # The api has a monthly limit, so work should be done to avoid using it when possible.
    
    # response = requests.get(url, headers=headers, params=querystring)
    response = requests.get(url, headers=headers)
    attributes = response.json()"""
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'saved': saved,
        'made': made,
        'liked': liked,
        # 'attributes': attributes,
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

def RecipeLiked(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    liked_recipe = Like.objects.filter(recipe = recipe).filter(user = request.user)
    if liked_recipe:
        liked_recipe.delete()
    else:
        Like.objects.create(user = request.user, recipe = recipe)
        
    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))
