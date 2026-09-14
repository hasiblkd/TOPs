from django.urls import path
from myapp.views import *

urlpatterns=[
    path("",index,name="index"),
    path("contect",contect,name="contect"),
    path("about",about,name="about")
]