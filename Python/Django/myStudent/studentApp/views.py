from django.shortcuts import render,redirect
from studentApp.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    data=request.POST
    id=data.get("id")
    s_name=data.get("s_name")
    s_email=data.get("s_email")
    s_age=data.get("s_age")

    if id:
        student=Student.objects.get(pk=id)
        student.s_name=s_name
        student.s_email=s_email
        student.s_age=s_age
        student.save()
        return render(request,"index.html",{"msg":"Update Succesfully..."})
    else:

        Student.objects.create(s_name=s_name,s_email=s_email,s_age=s_age)
        return render(request,"index.html",{"msg":"Registration Succesfully..."})

def display(request):
    student=Student.objects.all()
    return render(request,"display.html",{"student":student})

def delete(request):
    id=request.GET.get("id")
    st=Student.objects.get(id=id)
    st.delete()
    return redirect("display")

def update(request):
    id=request.GET.get("id")
    st=Student.objects.get(id=id)
    return render(request,"index.html",{"st":st})