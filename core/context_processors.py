from badges.models import AwardedBadge

def badges_to_display(request):
    if request.user.is_authenticated:
        badges_to_display = AwardedBadge.objects.filter(awarded_to = request.user).filter(displayed = False)
    else:
        badges_to_display = []
    return {'badges_to_display': badges_to_display,}