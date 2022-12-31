from djongo.models import (Model, CharField, TextField, DateTimeField, ForeignKey)
from djongo import models
from djongo.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.CharField(max_length=100)

class Post:
    title= models.CharField(max_length=255)
    body=models.TextField()
    category=models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now_add=True)

class Blog(Model):
    name = CharField(max_length=100)
    tagline = TextField()

    class Meta:
        abstract = True

class Comment(Model):
    author = CharField(max_length=60)
    body = TextField()
    created_on = DateTimeField(auto_now=True)
    item = ForeignKey(Gallery, on_delete=models.CASCADE)


class UserProfile(models.Model, UserManager):
    username = models.ForeignKey (Gallery, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.username

class User(AbstractBaseUser):
       objects =  UserManager()

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null = True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=False)
    msg = models.CharField(max_length=600, null=False)

    def __str__(self):
        return self.name
