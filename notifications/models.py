from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    # add the ability to add a url which will take you to the appropriate place
