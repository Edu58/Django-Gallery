from django.shortcuts import render
from .models import Categories, Locations, Images


# Create your views here.
def home(request):
    all_images = Images.objects.all()
    return render(request, 'index.html', {'all_images': all_images})


def search_by_category(request, category_name):
    images = Images.search_image(category_name)
    return render(request, 'search.html', {'images': images})
