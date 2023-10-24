from django.db import models
import random
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    phone=models.IntegerField()
    message=models.CharField(max_length=255)
    
    
    def __str__ (self):
        return self.name
    # to chnage name of object 
class Upload(models.Model):
    id=models.CharField(primary_key=True,max_length=1000000000000000000)
    description=models.TextField(max_length=255)
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    phone=models.CharField(max_length=13)
    photo=models.ImageField(upload_to='upload/')
    type1=models.CharField(max_length=20)
    inUse=models.DateField()
    def __str__ (self):
        return self.name
   

    




    
