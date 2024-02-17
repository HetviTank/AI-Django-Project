
from django.contrib import admin  
from django.urls import path 
from image_sharping.views import sharpen_image

urlpatterns = [
    path('sharpen_image/', sharpen_image, name='sharpen_image'),
]  