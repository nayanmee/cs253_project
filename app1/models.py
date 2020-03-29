from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django import forms


# Create your models here.


class Department(models.Model):
    Department_Name = models.CharField(max_length=100,unique=True)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

   


class demo(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class Profile(models.Model):
    Role_Choices = [
        ('Ta','Ta'),
        ('Manager','Manager'),
        ('Admin','Admin'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=Role_Choices,
        default='Ta'
        )

class Pending_Requests(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,blank=True)
    password=models.CharField(max_length=100)
    role = models.CharField(max_length=50,default = 'Ta')
    def __str__(self):
        return self.first_name
