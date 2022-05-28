from django.db import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


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

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls, image_id):
        try:
            cls.objects.filter(id=image_id).delete()
        except ObjectDoesNotExist:
            raise Http404
