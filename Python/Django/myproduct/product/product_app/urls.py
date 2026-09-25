from django.urls import path
from product_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",product,name="product"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete_product,name="delete"),
    path("update",update_product,name="update"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)