from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
