from django.db import models

# Create your models here.

class Student(models.Model):
    s_name=models.CharField(max_length=40)
    s_email=models.CharField(max_length=50)
    s_age=models.IntegerField()