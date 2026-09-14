from django.shortcuts import render
from dbapp.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def display(request):
    return render(request,"index.html")

def register(request):
    data=request.POST
    name=data.get("student_name")
    email=data.get("email")
    age=data.get("age")
    Student.objects.create(s_name=name,s_email=email,s_age=age)
    return render(request,"index.html",{"msg":"Registration Succfull..."})

def display(request):
    students=Student.objects.all()
    return render(request,"display.html",{"students":students})