from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
# Create your views here.
def home_view(request):
    return render(request, 'core/home.html')

def login_view(request):
   return render(request, 'core/login.html')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html',{
        'form': form,
    })