from django.contrib import admin
from apps.product.models import Product, ProductDetail


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'is_variation', 'brand_id', 'code',
                    'family', 'created', 'modified']
    search_fields = ['name', 'type']


admin.site.register(Product, ProductAdmin)


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'price', 'price_offer', 'offer_day_from',
                    'offer_day_to', 'quantity', 'sku', 'created',
                    'modified']
    search_fields = ['product__name','offer_day_from']


admin.site.register(ProductDetail, ProductDetailAdmin)
