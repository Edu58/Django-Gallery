from django.shortcuts import render, redirect
from .models import Categories, Locations, Images


# Create your views here.
def home(request):
    all_images = Images.objects.all()
    return render(request, 'index.html', {'all_images': all_images})


def search_by_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        print(category)
        all_images = Images.search_image(category)
        return render(request, 'index.html', {'all_images': all_images})
    return redirect('/home/')
