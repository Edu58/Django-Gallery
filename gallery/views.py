from django.shortcuts import render, redirect
from .models import Categories, Locations, Images


# Create your views here.
def home(request):
    all_images = Images.objects.all()
    return render(request, 'index.html', {'all_images': all_images})


def search_by_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        all_images = Images.search_image(category.capitalize())
        return render(request, 'index.html', {'all_images': all_images})
    return redirect('/')


def get_image_details(request, image_id):
    details = Images.get_image_by_id(image_id)
    return redirect('/', {'details': details})