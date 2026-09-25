from django.urls import path
from bookApp.views import *

urlpatterns=[
    path("",index,name="index"),
    path("register",register,name="regiister"),
    path("view_book",view_book,name="view_book"),
    path("delete_book",delete_book,name="delete_book"),
    path("update_book",update_book,name="update_book")
]