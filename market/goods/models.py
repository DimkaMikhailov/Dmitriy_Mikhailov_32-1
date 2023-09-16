from django.db.models import Model
from django.db import models


# Create your models here.
class CatalogGroup(Model):
    catalog_group_name = models.CharField(max_length=25)

    def __repr__(self):
        return self.catalog_group_name


class ProductCard(Model):
    catalog_group = models.ForeignKey(to=CatalogGroup, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='market/static/img', verbose_name='Product Image', blank=False, null=False)
    title = models.CharField(max_length=120)
    price = models.FloatField(verbose_name='Price')
    currency = models.CharField(max_length=5, default='$')
    description = models.TextField()
    in_stock = models.BooleanField(default=False)

    def __repr__(self):
        return f'Product={self.title}: price={self.price}{self.currency}, {self.catalog_group}, in_stock={self.in_stock}'
