from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntergerField(null = False)
    desc = models.TextField()
    pic = models.ImageField(upload_to = "products/", null = False)
    stock = models.PositiveIntegerField(default = 1)
    