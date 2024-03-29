import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class GenderType(models.IntegerChoices):
    """Модель типа пола пользователя"""
    MAN = 0
    WOMAN = 1


def upload_to(instance, filename: str):
    """Функция генерации пути аватарки"""
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.user.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class User(AbstractUser):
    """Модель пользователя juniorhunt"""
    username = models.SlugField('Никнейм пользователя', max_length=20, unique=True)
    phone = models.CharField('Номер телефона пользователя', max_length=15, unique=True)
    email = models.EmailField('Email пользователя', unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя пользователя', max_length=30)
    last_name = models.CharField('Фамилия пользователя', max_length=30)
    second_name = models.CharField('Отчество пользователя', max_length=30, blank=True, null=True)
    is_company = models.BooleanField('Является ли пользователь представителем компании', default=False)
    company_name = models.CharField('Название компании', max_length=50, blank=True, null=True)
    description = models.TextField('Описание')
    gender = models.IntegerField('Пол', choices=GenderType.choices, default=0)
    contacts = models.TextField('Контакты', blank=True, null=True)
    address = models.TextField('Адрес', null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'profile_users'


class UserNotification(models.Model):
    user = models.OneToOneField(ProfileUser, on_delete=models.CASCADE)
    token = models.TextField('Токен пользователя')

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Токен уведомлений пользователя'
        verbose_name_plural = 'Токены управления пользователей'
        db_table = 'notification_token_users'
