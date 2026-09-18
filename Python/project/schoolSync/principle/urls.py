from django.urls import path
from principle.views import *

urlpatterns=[
    path("",principle_dashbored,name="principle_dashbored"),
    path("principle_student",principle_student,name="principle_student")
]