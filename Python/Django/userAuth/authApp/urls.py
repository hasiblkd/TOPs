from django.urls import path
from authApp.views import *

urlpatterns=[

    path("",user_logging,name="logging"),
    path("registration",registration,name="registration"),
    path("logout",user_logout,name="logout"),
    path("home",home,name="home")

]