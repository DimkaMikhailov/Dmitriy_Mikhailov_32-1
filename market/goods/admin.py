from django.contrib import admin

from goods.models import CatalogGroup, ProductCard
# Register your models here.

admin.site.register(CatalogGroup)
admin.site.register(ProductCard)
