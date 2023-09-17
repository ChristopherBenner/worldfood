from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm

from django.contrib.auth.models import User
from dashboard.models import Dashboard
# Create your views here.
def home_view(request):
    return render(request, 'core/home.html')

def login_view(request):
   return render(request, 'core/login.html')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            user = User.objects.filter(username = username).first()
            # Create a dashboard instance upon creation of an account
            Dashboard.objects.create(user = user)
            return redirect('/login/')
        
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html',{
        'form': form,
    })