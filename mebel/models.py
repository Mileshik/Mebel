from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="Назва")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"




class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    poster = models.URLField(default="http://placehold.it/100x100", verbose_name= "Постер")


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    def __str__(self):
        return f"{self.user} - {self.items}"

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карти"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



# Create your models here.
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"

