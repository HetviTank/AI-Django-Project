
from django.contrib import admin  
from django.urls import path 
from login.views import login

urlpatterns = [  
    path('', login, name='login'),
]  