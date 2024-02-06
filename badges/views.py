from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import AwardedBadge, Badge

# Create your views here.
def view_badges(request):
    pass
    # get a list of badges awarded by each user
    badges = Badge.objects.all()
    awarded_badges = AwardedBadge.objects.filter(awarded_to = request.user)
    return render(request, 'badges/badges.html', {
        'badges': badges,
        'awarded_badges': awarded_badges,
    })

def badge_displayed(request, recipe_id, badge_id):
    badge = AwardedBadge.objects.filter(pk = badge_id).exists()
    if badge:
        badge = AwardedBadge.objects.filter(pk = badge_id).first()
        badge.displayed = True
        badge.save()
    return redirect(reverse('recipes:recipe_redirect', args=[str(recipe_id)]))
'''
def RecipeSave(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    saved_recipe = SavedRecipe.objects.filter(recipe = recipe).filter(user = request.user)
    if saved_recipe:
        saved_recipe.delete()
    else:
        SavedRecipe.objects.create(user = request.user, recipe = recipe)

    return redirect(reverse('recipes:recipe_redirect', args=[str(pk)]))
'''