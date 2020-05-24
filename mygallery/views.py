from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    return render(request, 'index.html',{})

def get_category(request):
    return render(request, 'index.html',{})

def get_location(request):
    return render(request, 'index.html',{})