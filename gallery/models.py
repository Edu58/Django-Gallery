from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=30)

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

    def __str__(self):
        return self.name
