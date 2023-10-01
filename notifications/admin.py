from django.contrib import admin
from .models import Notification, NotificationCategory


admin.site.register(Notification)
admin.site.register(NotificationCategory)
