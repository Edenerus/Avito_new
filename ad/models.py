from django.db import models

from user.models import User
from django.core.validators import MinLengthValidator


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=10, validators=[MinLengthValidator(5)], unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)],)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
