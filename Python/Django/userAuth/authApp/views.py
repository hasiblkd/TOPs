from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_logging(request):
    if request.method=="POST":
        data=request.POST
        uname=data.get("username")
        password=data.get("password")

        user=authenticate(username=uname,password=password)

        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"logging.html",{"err1":"Invalid User...."})
    else:
        return render(request,"logging.html")


def registration(request):
    if request.method=="POST":
        data=request.POST
        fname=data.get("first_name")
        lname=data.get("last_name")
        uname=data.get("username")
        password=data.get("password")

        if User.objects.filter(username=uname).exists():
            return render(request,"registration.html",{"err2":"User Already Exist....."})

        User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)

        return render(request,"registration.html",{"msg":"Registration Succesfully..."})

    return render(request,"registration.html")

def user_logout(request):
    logout(request)
    return redirect("logging")

@login_required(login_url="logging")
def home(request):
    return render(request,"home.html")