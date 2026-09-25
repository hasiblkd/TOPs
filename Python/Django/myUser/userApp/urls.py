from django.urls import path
from userApp.views import *

urlpatterns=[
    path("",user_login,name="login"),
    path("register",user_register,name="register"),
    path("home",user_home,name="home"),
    path("logout",user_logout,name="logout")
]