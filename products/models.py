from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    

class Product(models.Model):
    collection = models.ForeignKey('Collection', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    height =  models.DecimalField(max_digits=6, decimal_places=2)
    width =  models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=60, null=False, blank=False)
    review = models.TextField(null=False, blank=False)
    RATING_CHOICES = (
        ("0", 'No rating'),
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
    )
    rate = models.IntegerField(choices=RATING_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
