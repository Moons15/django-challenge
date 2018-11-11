from django.db.models import *
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from enum import Enum


class ProductQuerySet(models.QuerySet):
    pass


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Product(models.Model):
    class TYPE(Enum):
        PR = "PR"
        SR = "SR"

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    type = models.CharField(max_length=2,
                            choices=[(item.name, item.value) for item in
                                     TYPE])
    name = models.CharField(max_length=200, )
    description = models.TextField()
    is_variation = models.BooleanField(default=False)
    # TODO: It should be a foreign key, however, I don't have too much information
    brand_id = models.IntegerField()
    code = models.IntegerField()
    family = models.IntegerField()
    is_complement = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('created',)

    def __str__(self):
        return '{} - code: {} -id:{}'.format(self.name, self.code, self.id)


class ProductDetailQuerySet(models.QuerySet):
    pass


class ProductDetailManager(models.Manager):
    def get_queryset(self):
        return ProductDetailQuerySet(self.model, using=self._db)


class ProductDetail(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_visibility = models.BooleanField(default=True)
    price = models.FloatField()
    price_offer = models.FloatField(blank=True, null=True)
    offer_day_from = models.DateTimeField(auto_now_add=True, blank=True,
                                          null=True)
    offer_day_to = models.DateTimeField(auto_now_add=True, blank=True,
                                        null=True)
    quantity = models.IntegerField()
    sku = models.IntegerField()
    product = models.ForeignKey(Product, related_name='product_details',
                                on_delete=CASCADE)

    class Meta:
        verbose_name = "Product Detail"
        verbose_name_plural = "Product Details"
        ordering = ('created',)

    def __str__(self):
        return '{} - price: {}'.format(self.product, self.price)
