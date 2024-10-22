from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2)
