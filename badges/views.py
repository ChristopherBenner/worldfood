from django.shortcuts import render
# from .models import AwardedBadge, Badge

# Create your views here.
def view_badges(request):
    pass
    # get a list of badges awarded by each user
    badges = Badge.objects.all()
    awarded_badges = AwardedBadge.objects.filter(awarded_to = request.user)
    return render(request, 'badges/badges.html', {
        'badges': badges,
        'awarded_badges': awarded_badges,
    })