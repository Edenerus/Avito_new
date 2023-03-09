from django.contrib.auth.models import AbstractUser
from django.db import models

from user.validators import check_email, check_birth_date


class Location(models.Model):

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    name = models.CharField(max_length=30)
    is_activate = models.BooleanField(default=True, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"

    STATUS = [
        (MEMBER, "Гость"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Администратор")
    ]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    role = models.CharField(max_length=9, choices=STATUS, default='member', null=True)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True, blank=True, validators=[check_birth_date])
    email = models.EmailField(unique=True, null=True, validators=[check_email])

    def __str__(self):
        return self.username
