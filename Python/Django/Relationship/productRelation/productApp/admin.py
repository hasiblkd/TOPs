from django.contrib import admin
from productApp.models import *

# Register your models here.

class CategoryDisplay(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['name']
    list_filter=['name']

class ProductDisplay(admin.ModelAdmin):
    list_display=['id','name','qty','price']
    search_fields=['name']
    list_filter=['name']
    

admin.site.register(Category,CategoryDisplay)
admin.site.register(Product,ProductDisplay)