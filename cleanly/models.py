from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    header = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    pic = models.ImageField(upload_to = 'images/', null=True)

    def __unicode__(self):
        return self.header

class History(models.Model):
    user = models.ForeignKey(User)
    product_id = models.IntegerField(default=0)
    product_header = models.CharField(max_length=20)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.product_header
