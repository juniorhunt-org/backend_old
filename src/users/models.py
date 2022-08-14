import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class GenderType(models.IntegerChoices):
    """Модель типа пола пользователя"""
    MAN = 0
    WOMAN = 1


class User(AbstractUser):
    """Модель пользователя juniorhunt"""
    first_name = models.CharField('Имя пользователя', max_length=30)
    last_name = models.CharField('Фамилия пользователя', max_length=30)
    second_name = models.CharField('Отчество пользователя', max_length=30, blank=True, null=True)
    gender = models.IntegerField('Пол пользователя', choices=GenderType.choices, default=0)
    address = models.TextField('Адрес проживания пользователя', null=True, blank=True)
    phone = models.CharField('Номер телефона пользователя', max_length=15, unique=True)
    email = models.EmailField('Email пользователя', unique=True)
    is_staff = models.BooleanField('Персонал сайта', default=False)
    created_at = models.DateTimeField('Дата создания аккаунта', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления данных аккаунта', auto_now=True)

    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.second_name)
        return full_name.strip()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'


def upload_to(instance, filename: str):
    """Функция генерации пути аватарки"""
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.user.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class UserAvatar(models.Model):
    """Модель аватарки пользователя"""
    avatar = models.ImageField('Аватар пользователя', upload_to=upload_to)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.user.get_full_name()} avatar"

    class Meta:
        verbose_name = 'Аватар пользователя'
        verbose_name_plural = 'Аватары пользователей'
        db_table = 'users_avatar'
