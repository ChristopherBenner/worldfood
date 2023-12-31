# Generated by Django 4.2.5 on 2023-09-16 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dashboard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "made_recipes",
                    models.ManyToManyField(
                        related_name="made_recipes", to="recipes.recipe"
                    ),
                ),
                (
                    "saved_recipes",
                    models.ManyToManyField(
                        related_name="saved_recipes", to="recipes.recipe"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dashboard",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
