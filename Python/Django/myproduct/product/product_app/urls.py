from django.urls import path
from product_app.views import *


urlpatterns=[
    path("",product,name="product"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete_product,name="delete"),
    path("update",update_product,name="update")
]