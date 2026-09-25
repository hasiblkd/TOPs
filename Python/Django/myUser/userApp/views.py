from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method=="POST":
        data=request.POST
        u_name=data.get("username")
        u_password=data.get("password")

        user=authenticate(username=u_name,password=u_password)

        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{"err":"User Not Exist...."})
    else:
        return render(request,"login.html")


def user_register(request):
    if request.method=="POST":
        data=request.POST
        f_name=data.get("first_name")
        l_name=data.get("last_name")
        u_name=data.get("username")
        u_password=data.get("password")

        if User.objects.filter(username=u_name).exists():
            return render(request,"register.html",{"msg":"User Already exist...."})

        User.objects.create_user(first_name=f_name,last_name=l_name,username=u_name,password=u_password)

        return render(request,"register.html",{"msg1":"Registration Succesfully..."})
    return render(request,"register.html")

@login_required(login_url="login")
def user_home(request):
    return render(request,"home.html")


def user_logout(request):
    logout(request)
    return redirect("login")