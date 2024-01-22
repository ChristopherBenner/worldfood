# notifications/serializers.py
from rest_framework import serializers

from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "category",
            "user",
            "notification_time",
            "read",
        )
        model = Notification