# Generated by Django 4.2.5 on 2024-01-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("countries", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="country",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
