# Generated by Django 4.2.5 on 2024-02-07 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0007_remove_badge_displayed_awardedbadge_displayed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="awardedbadge",
            name="badge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="badges",
                to="badges.badge",
            ),
        ),
    ]
