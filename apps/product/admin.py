from django.contrib import admin
from apps.product.models import Product, ProductDetail


admin.site.register(Product)
admin.site.register(ProductDetail)
