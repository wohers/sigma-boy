from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    img = models.ImageField(upload_to='products/', verbose_name="Изображение", null=True, blank=True)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title
