# notifications/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Notification
@login_required
def view_notifications(request):
    notifications = Notification.objects.filter(user = request.user)
    return render(request, 'notifications/notifications.html',{
        'notifications': notifications,
    })

@login_required
def notifications_clear(request):
    notifications = Notification.objects.filter(user = request.user).filter(read = False)
    for notification in notifications:
        notification.read = True
        notification.save()
    return redirect(reverse('notifications:notifications'))

@login_required
def notification_read(request, pk):
    notification = Notification.objects.filter(user = request.user).filter(pk = pk).first()
    notification.read = True
    notification.save()
    return redirect(reverse('notifications:notifications'))


