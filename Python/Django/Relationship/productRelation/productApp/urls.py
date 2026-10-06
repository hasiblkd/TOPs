from django.urls import path
from productApp.views import *

urlpatterns=[

    path("",index,name="index"),
    path("register",register,name="register")

]