from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.core.validators import MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        self.name

class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        self.name

class Product(models.Model):
    photo = models.URLField(max_length=500)
    asin = models.CharField(unique=True, max_length=100)
    seller = models.ForeignKey(Seller,  on_delete=CASCADE, related_name='products')
    price = models.FloatField(validators=[MaxValueValidator(0)])
    title =  models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='products')
    updated = models.DateTimeField(auto_now_add=True)