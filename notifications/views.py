# notifications/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def view_notifications(request):
    return render(request, 'notifications/notifications.html')