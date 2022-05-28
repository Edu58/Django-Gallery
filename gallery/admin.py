from django.contrib import admin
from .models import Categories, Locations, Images

# Register your models here.
admin.site.register([Categories, Locations, Images])
