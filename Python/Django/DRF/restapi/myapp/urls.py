from django.urls import *
from myapp.views import *

urlpatterns = [

    path("create",create),


    path("list-student",list_student)

]