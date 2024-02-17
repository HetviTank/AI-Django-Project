from django.shortcuts import render,redirect
from .models import user
from django.http import HttpResponseRedirect
def login_view(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        password = request.POST.get('password')
        user.objects.create(firstname=firstname, password=password)
        return HttpResponseRedirect('/dashboard/')
    return render(request, 'login.html')