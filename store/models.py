from typing import Any
from django.db import models

# Create your models here.
class Name(models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.name = models.CharField(max_length=255, db_index=True)
        self.slug = models.SlugField(max_length=250, unique=True)
        
    class Meta:
        # override django's defualt behaviour to avoid categorys 
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.title = models.CharField(max_length=250)
        self.brand = models.CharField(max_length=250, default='un-branded')
        self.description = models.TextField(blank=True)
        self.slug = models.SlugField(max_length=255)
        self.price = models.DecimalField(max_digits=4, decimal_places=2)
        self.image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
