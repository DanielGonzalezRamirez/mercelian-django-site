from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/02_home.html', {'title': 'Home'})

def paula(request):
    return render(request, 'main/03_paula.html', {'title': 'Paula'})

def daniel(request):
    return render(request, 'main/04_daniel.html', {'title': 'Daniel'})
