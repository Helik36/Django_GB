from django.contrib import admin

from mainapp.models import ProductCategory, Product, Location

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Location)