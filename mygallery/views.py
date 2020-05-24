from django.shortcuts import render
from django.http  import HttpResponse, Http404
from mygallery.models import Image, Category, Location

# Create your views here.
def welcome(request):
    all_images = Image.objects.all()
    all_categories = Category.objects.all()
    all_locations = Location.objects.all()
    return render(request, 'index.html',{'all_images': all_images, 'all_categories': all_categories, 'all_locations' : all_locations})

def get_category(request,category):
    categ = Category.objects.all()
    search_cats = Image.objects.filter(category__title = category)
    message = f"{category}"
    return render(request, 'index.html',{'categ':categ, 'search_cats':search_cats, 'message':message})

def get_location(request,location):
    loca = Location.objects.all()
    search_loca = Image.objects.filter(location__country = location)
    message = f"{location}"
    return render(request, 'index.html',{'search_loca':search_loca, 'loca':loca, 'message':message})


def navlocation(request):

    categ = Category.objects.all()
    loca = Location.get_location()

    return render(request, 'navbar.html', {"loca": loca, 'categ':categ})
