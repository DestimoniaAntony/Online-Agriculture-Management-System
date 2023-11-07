from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)
    
class Farmer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    mobile = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    req_quantity = models.IntegerField(null=True)
    
class Researcher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=50,null=True)
    qualification = models.CharField(max_length=50,null=True)
    
class Crop(models.Model):
    crop = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='media/',null=True)
    description = models.CharField(max_length=50,null=True)
    total_quantity = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    
    
class Fertilizer(models.Model):
    fertilizer = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='media/',null=True)
    description = models.CharField(max_length=50,null=True)
    total_quantity = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    
class Subsidy(models.Model):
    description = models.CharField(max_length=5000,null=True)

class Booking(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE,null=True)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Farmer, on_delete=models.CASCADE,null=True)
    payment = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    amount = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    
class FarmingTechnique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()