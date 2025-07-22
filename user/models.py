from django.db import models

class users(models.Model):
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    role=models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)