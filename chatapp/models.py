from django.db import models
from datetime import datetime

# Create your models here.
class chater(models.Model):
    name=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    
class Message(models.Model):
    value=models.CharField(max_length=10000000000000000)
    data=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=10000000000000000)
    room=models.CharField(max_length=10000000000000000)

class ichater(models.Model):
    username= models.CharField(max_length=10000)
    messageaya= models.CharField(max_length=100000000000000000 ,default='nothing', )
    
    