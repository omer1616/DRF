import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_product")
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    relase_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        # db_table = 'Product_test'
        # ordering = ['created_date']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"Products/{self.slug}"
        return reverse('product_detail', kwargs={'id': self.id})




EVALUATION = (
    ('1', 'Kötü'),
    ('2', 'Eh İşte'),
    ('3', 'İdare Eder'),
    ('4', 'İyi'),
    ('5', 'Çok iyi'),

)


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Kitap", on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    evulation = models.CharField(max_length=25, choices=EVALUATION, default=5)

    def __str__(self):
        return f" {self.product} - {self.user} - {self.comment}"
