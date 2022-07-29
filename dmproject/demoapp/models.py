from django.db import models


# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='img')
    dec= models.TextField()

class product(models.Model):
    name=models.CharField(max_length=400)
    img=models.ImageField(upload_to='img2')
    dec=models.TextField()
    link=models.URLField()
