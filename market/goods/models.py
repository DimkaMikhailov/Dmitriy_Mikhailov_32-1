from django.db.models import Model
from django.db import models
from django.contrib.auth.models import User


RATING_CHOICES = (
    (1, 'Terrible'),
    (2, 'Bad'),
    (3, 'Normal'),
    (4, 'Good'),
    (5, 'Perfect'))


class CatalogGroup(Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='img/categories/',
                            verbose_name='Category Image',
                            blank=False,
                            null=False)

    alt = models.TextField(max_length=25)

    def __str__(self):
        return self.name


class ProductCard(Model):
    catalog_group = models.ManyToManyField(to=CatalogGroup, related_name='products')

    image = models.ImageField(upload_to='img/', verbose_name='Product Image', blank=False, null=False)
    title = models.CharField(max_length=120)
    price = models.FloatField(verbose_name='Price')
    currency = models.CharField(max_length=5, default='$')
    description = models.TextField()
    in_stock = models.BooleanField(default=False)
    count = models.IntegerField(verbose_name='Amount')
    author = models.ForeignKey(to=User, related_name='user', on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f'Product={self.title}: price={self.price}{self.currency}, in_stock={self.in_stock}'

    def __str__(self):
        return self.title


class ProductReviews(Model):
    review = models.TextField(verbose_name='Review')
    rating = models.FloatField(verbose_name='Rating')

    product_id = models.ForeignKey(to=ProductCard, on_delete=models.DO_NOTHING, related_name='product_id')

    def __repr__(self):
        return f'{self.review}'

