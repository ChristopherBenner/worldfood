from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from restcountries import RestCountryApiV2 as rapi

import requests, json
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

def recipe_list(request, pk, slug):
    country_name = Country.objects.filter(pk=pk).first()
    country_list = rapi.get_countries_by_name(country_name)
    country = country_list[0]
    recipes = list(Recipe.objects.filter(country = country_name))

    """url = "https://yummly2.p.rapidapi.com/feeds/search"
    querystring = {"q":country}

    # The API Key should be moved into a separate file, and not included in the main files
    headers = {"X-RapidAPI-Key": "395ac24211msh69d8d498a22b082p1bf25djsn81214c5dc50b",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # Uncomment the lines below to access the api -> Not used during testing
    # The api has a monthly limit, so work should be done to avoid using it when possible.
    
    response = requests.get(url, headers=headers, params=querystring)
    attributes = response.json()
    web_recipes = attributes["feed"]
    """

    # Remove the following lines when moving out of testing
    """with open("./jsonformatter.txt",'r') as country_file:
        country_data = json.load(country_file)

    web_recipes = country_data["feed"]"""
    
    




    return render(request, 'countries/recipe_list.html', {
        'recipes': recipes,
        'country': country,
        # 'web_recipes': web_recipes,
    })

def get_redirect_url(request, pk):
    country = Country.objects.get(pk=pk)
    slug = country.slug
    return redirect(reverse("countries:recipe_list", args=(pk, slug)))