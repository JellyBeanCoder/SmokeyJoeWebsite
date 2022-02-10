from ftplib import all_errors
from django.shortcuts import render
from .models import Joe

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def collection(request):
    all_joe = Joe.objects.all()
    return render(request, 'collection.html', {"all_joe" : all_joe})