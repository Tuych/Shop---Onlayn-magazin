from django.db import models
from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='категория')
    description = models.TextField(blank=True, verbose_name='Опесание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    image = models.ImageField(upload_to="products_images/", blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=100, blank=True, verbose_name='Краткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    add_photo = models.ImageField(upload_to="products_images/add/", blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображении'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ползователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0)   # manfiy sonlarni qabul qilmaydi
    create_database = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"корзина для {self.user.username} | Продукт {self.product.name}"

    def sum(self):
        return self.quantity * self.product.price   # Metodlarni HTML stranirsada chaqirsa ham buladi


    class Meta:
        verbose_name = 'товар в корзину'
        verbose_name_plural = 'корзина'


