# Generated by Django 4.2.5 on 2024-01-06 11:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0005_remove_recipe_made_recipes_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="maderecipe",
            options={"verbose_name_plural": "Made Recipes"},
        ),
        migrations.AlterModelOptions(
            name="savedrecipe",
            options={"verbose_name_plural": "Saved Recipes"},
        ),
    ]
