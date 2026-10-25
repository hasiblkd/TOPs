from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *

# Create your views here.

@api_view(['POST '])
def create(request):
    return Response("Api Calling")



def list_student(request):
    students=Student.objects.all()
    ser=StudentSerializer(students,many=True)
    return Response({"data":ser.data})