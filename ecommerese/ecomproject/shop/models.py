from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product_by_category', arg=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

