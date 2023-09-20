from django.db.models import Model
from django.db import models


# Create your models here.
class CatalogGroup(Model):
    catalog_group_name = models.CharField(max_length=25)
    category_img = models.ImageField(upload_to='img/categories/',
                                     verbose_name='Category Image',
                                     blank=False,
                                     null=False)

    def __str__(self):
        return self.catalog_group_name


class ProductCard(Model):
    catalog_group = models.ManyToManyField(to=CatalogGroup, related_name='products')

    image = models.ImageField(upload_to='img/', verbose_name='Product Image', blank=False, null=False)
    title = models.CharField(max_length=120)
    price = models.FloatField(verbose_name='Price')
    currency = models.CharField(max_length=5, default='$')
    description = models.TextField()
    in_stock = models.BooleanField(default=False)
    count = models.IntegerField(verbose_name='Amount')

    def __repr__(self):
        return f'Product={self.title}: price={self.price}{self.currency}, in_stock={self.in_stock}'

    def __str__(self):
        return self.title
