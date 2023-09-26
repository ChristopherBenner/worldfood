from .models import Notification

def notification_processor(request):
    num_notifications = ''
    if request.user.is_authenticated:
        count = Notification.objects.filter(user = request.user).count()
        if count > 0:
            num_notifications = count
    
        
    
    return {'num_notifications':num_notifications}