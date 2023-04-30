from typing import Any
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, default="un-categorized")
    slug = models.SlugField(max_length=250, unique=True, default="un-categorized")
        
    class Meta:
        # override django's defualt behaviour to avoid categorys 
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250, default="un-titled-product")
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, default="no-product")
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
