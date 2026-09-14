from django.db import models

# Create your models here.

class Student(models.Model):
    s_name=models.CharField(max_length=25)
    s_email=models.CharField(max_length=40)
    s_age=models.IntegerField()


class product(models.Model):
    p_name=models.CharField(max_length=50)
    p_qty=models.IntegerField()
    p_price=models.FloatField()