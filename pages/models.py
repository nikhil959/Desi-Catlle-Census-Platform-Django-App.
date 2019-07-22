from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.

class Post1(models.Model):
    title= models.TextField()
    content= models.TextField()


class newaccount1(models.Model):
    username= models.TextField()
    password= models.TextField()
    email= models.TextField()



class newaccount2(models.Model):
    username= models.TextField()
    password= models.TextField()
    email= models.TextField()
    
class Post12(models.Model):
      
      
      breedname=models.CharField(max_length=200)
      counts=models.CharField(max_length=200)
      ownername=models.CharField(max_length=200)
      email=models.CharField(max_length=200)
      aadharcard=models.CharField(max_length=200)
      phonenumber=models.CharField(max_length=200)
      location=models.CharField(max_length=200)
      animaltype= models.CharField(max_length=200)

class Post13(models.Model):
      
      
      breedname=models.CharField(max_length=200)
      counts=models.CharField(max_length=200)
      ownername=models.CharField(max_length=200)
      email=models.CharField(max_length=200)
      aadharcard=models.CharField(max_length=200)
      phonenumber=models.CharField(max_length=200)
      location=models.CharField(max_length=200)
      animaltype= models.CharField(max_length=200)
      







class Imageupload(models.Model):
      
      img1=models.ImageField(upload_to='images/',blank=True)
class Imageupload1(models.Model):
      
      img1=models.ImageField(upload_to='images/',blank=True)
      
class upload(models.Model):
      breedname=models.CharField(max_length=200)
      counts=models.CharField(max_length=200)
      ownername=models.CharField(max_length=200)
      email=models.CharField(max_length=200)
      aadharcard=models.CharField(max_length=200)
      phonenumber=models.CharField(max_length=200)
      location=models.CharField(max_length=200)
      animaltype= models.CharField(max_length=200)
      img1=models.ImageField(upload_to='images/',blank=True)