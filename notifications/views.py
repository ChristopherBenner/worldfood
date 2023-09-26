# notifications/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Notification
@login_required
def view_notifications(request):
    notifications = Notification.objects.filter(user = request.user)
    return render(request, 'notifications/notifications.html',{
        'notifications': notifications,
    })