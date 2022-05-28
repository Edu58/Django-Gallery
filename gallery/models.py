from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404


# Create your models here.
class Categories(models.Model):
    CATEGORY_CHOICES = [
        ('Nature', 'Nature'),
        ('Vehicles', 'Vehicles'),
        ('People', 'People'),
        ('Sky', 'Sky'),
        ('Animals', 'Animals'),
    ]

    name = models.CharField(max_length=12, choices=CATEGORY_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.name


class Locations(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def update_image(self, image_id):
        pass

    @classmethod
    def delete_image(cls, image_id):
        image_to_delete = get_object_or_404(cls, id=image_id)
        image_to_delete.delete()

    @classmethod
    def get_image_by_id(cls, image_id):
        image = get_object_or_404(cls, id=image_id)
        return image

    @classmethod
    def search_image(cls, category):
        images = Images.objects.filter(category__name=category)
        if len(images) == 0:
            return 'Category does no exist'
        else:
            return images

    @classmethod
    def filter_by_location(cls, location):
        images = Images.objects.filter(location__name=location)
        if len(images) == 0:
            return 'No images from that location'
        else:
            return images
