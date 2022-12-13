from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    mini_description = models.TextField()
    create_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now_add=True)
    reting = models.FloatField(blank=True, null=True)