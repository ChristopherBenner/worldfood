# Generated by Django 4.2.5 on 2023-09-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
