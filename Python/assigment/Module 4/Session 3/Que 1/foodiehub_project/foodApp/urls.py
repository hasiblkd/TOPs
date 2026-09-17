from django.urls import path
from foodApp.views import *

urlpatterns=[
    path("",index,name="index"),
    path("home",home,name="home"),
    path("explore",explore,name="explore")
]