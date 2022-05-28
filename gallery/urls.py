from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_by_category, name='search'),
    path('image-details/<int:image_id>', views.get_image_details, name='image-details')
]
