from django.contrib import admin
from .models import BadgeCategory, Badge, AwardedBadge
# Register your models here.
admin.site.register(Badge)
admin.site.register(BadgeCategory)
admin.site.register(AwardedBadge)