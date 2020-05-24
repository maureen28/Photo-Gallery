from django.shortcuts import render
from django.http  import HttpResponse
from mygallery.models import Image,Category, Location

# Create your views here.
def welcome(request):
    all_images = Image.objects.all()
    all_categories = Category.objects.all()
    all_locations = Location.objects.all()
    return render(request, 'index.html',{'all_images': all_images, 'all_categories': all_categories, 'all_locations' : all_locations})

def get_category(request):
    return render(request, 'index.html',{})

def get_location(request):
    return render(request, 'index.html',{})