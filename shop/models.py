from django.db import models

from blog.models import Post


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveBigIntegerField(default=0)
    available = models.BooleanField(default=True)
    posts = models.ManyToManyField(Post, related_name='products')

    def __str__(self):
        return self.name
