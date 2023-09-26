from django.shortcuts import render

# Create your views here.
def view_badges(request):
    return render(request, 'badges/badges.html')