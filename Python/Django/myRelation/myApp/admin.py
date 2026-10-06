from django.contrib import admin
from myApp.models import *

# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    list_display=['id','name','price','qty']

    search_fields=['name']

    list_filter=['name']

admin.site.register(Country)
admin.site.register(Capital)


admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Student)
admin.site.register(Course)


