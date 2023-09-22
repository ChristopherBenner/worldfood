from django.contrib import admin

# Register your models here.
from .models import Recipe, SavedRecipe, MadeRecipe

admin.site.register(Recipe)
admin.site.register(SavedRecipe)
admin.site.register(MadeRecipe)