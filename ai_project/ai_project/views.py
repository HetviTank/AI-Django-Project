from django.shortcuts import render
def home(request):
    # Add any necessary logic here
    return render(request, 'index.html')