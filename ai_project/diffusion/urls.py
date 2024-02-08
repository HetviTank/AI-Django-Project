
from django.contrib import admin  
from django.urls import path 
from diffusion.views import text2image_view

urlpatterns = [  
    path('admin/', admin.site.urls), 
    path('text2image_view/', text2image_view, name='text2image_view'),
]  