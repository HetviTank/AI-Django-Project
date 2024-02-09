from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
def home(request):
    # Add any necessary logic here
    return render(request, 'index.html')