# Generated by Django 4.2.5 on 2024-01-13 10:56

import badges.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="badge_category",
            field=models.ForeignKey(
                blank=True,
                default=badges.models.get_category,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="badges.badgecategory",
            ),
        ),
    ]
