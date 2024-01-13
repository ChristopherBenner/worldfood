from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''class NotificationCategory(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Notification Categories'

    def __str__(self):
        return self.category'''

class Notification(models.Model):
    categories = (("badge awarded", "Badge Awarded"),)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length = 255, choices = categories, null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    # add the ability to add a url which will take you to the appropriate place

    def __str__(self):
        return f"{self.category} | {self.description}"