from django.shortcuts import render
from .models import Categories, Locations, Images


# Create your views here.
def home(request):
    all_images = Images.objects.all()
    return render(request, 'index.html', {'all_images': all_images})
