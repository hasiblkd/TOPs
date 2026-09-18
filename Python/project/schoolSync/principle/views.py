from django.shortcuts import render

# Create your views here.

def principle_dashbored(request):
    return render(request,"principle/dashboard.html")

def principle_student(request):
    return render(request,"principle/student.html")