
from django.contrib import admin  
from django.urls import path 
from convertor.views import ExcelToJsonView

urlpatterns = [  
    path('admin/', admin.site.urls), 
    path('excel-to-json/', ExcelToJsonView.as_view(), name='excel_to_json'),
]  