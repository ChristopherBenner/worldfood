from django.apps import apps
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BadgeCategory(models.Model):
    category = models.CharField(max_length = 255)

    class Meta():
        verbose_name_plural = 'Badge Categories'

    def __str__(self):
        return self.category

def get_category():
    return BadgeCategory.objects.get_or_create(id = '1', category = 'test category')

class Badge(models.Model):
    badge_category = models.ForeignKey(BadgeCategory, default = get_category, on_delete = models.CASCADE, null=True, blank=True)
    badge_name = models.CharField(max_length = 255)
    awarded_badge = models.ImageField(upload_to="static/badges", null=True, blank=True)
    not_awarded_badge = models.ImageField(upload_to="static/badges", null=True, blank=True)
    points_required = models.IntegerField(null = True, blank = True)
    

    def __str__(self):
        return self.badge_name

class AwardedBadge(models.Model):
    badge = models.ForeignKey(Badge, on_delete = models.CASCADE)
    awarded_to = models.ForeignKey(User, on_delete = models.CASCADE)
    date_awarded = models.DateTimeField(auto_now_add = True)
    displayed = models.BooleanField(default=False)

    class Meta:
        unique_together = (('badge', 'awarded_to'),)
    def __str__(self):
        return self.badge.badge_name + " | " + self.awarded_to.username