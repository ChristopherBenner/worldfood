from django.db.models import Q
from django.shortcuts import render

from .models import Continent, Country
from recipes.models import Recipe
# Create your views here.
def country_list(request):
    continents = list(Continent.objects.all())
    countries = list(Country.objects.all())
    query = request.GET.get('query','')

    if query:
        countries = Country.objects.filter(Q(name__icontains = query) | Q(continent__name__icontains = query))
        continents = []
        for country in countries:
            continents.append(country.continent)

    return render(request, 'countries/countries_homepage.html',{
        'continents': continents,
        'countries': countries,
        'query': query,
    })

def recipe_list(request, pk):
    # country = Country.objects.filter(pk=pk).first()
    # recipes = list(Recipe.objects.filter(country = country))
    recipes = list(Recipe.objects.all())
    return render(request, 'countries/recipe_list.html', {
        'recipes': recipes,
    })