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
    images = Image.search_by_category(category)
    all_categories = Category.objects.all()
    message = f"{category}"
    return render(request, 'index.html', {"message":message, "images":images, 'categories': all_categories})


def get_location(request, location ):
    images = Image.filter_by_location(location)
    all_locations = Location.objects.all()
    message = f"{location}"
    return render(request, 'index.html', {"message":message, "images":images, "locations":all_locations})


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categorys": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{ 'message': message})

def navlocation(request):
    all_categories = Category.objects.all()
    all_locations = Location.objects.all()
    return render(request, 'navbar.html', {"locations": all_locations, 'categories':all_categories})
