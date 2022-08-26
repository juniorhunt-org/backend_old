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


class SchoolUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя пользователя', max_length=30)
    last_name = models.CharField('Фамилия пользователя', max_length=30)
    second_name = models.CharField('Отчество пользователя', max_length=30, blank=True, null=True)
    gender = models.IntegerField('Пол пользователя', choices=GenderType.choices, default=0)
    address = models.TextField('Адрес проживания пользователя', null=True, blank=True)
    avatar = models.ImageField('Аватар пользователя', upload_to=upload_to, blank=True, null=True)
    description = models.TextField('Описание пользователя')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь школьник'
        verbose_name_plural = 'Пользователи школьники'
        db_table = 'school_users'


class EmployerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя пользователя', max_length=30)
    last_name = models.CharField('Фамилия пользователя', max_length=30)
    second_name = models.CharField('Отчество пользователя', max_length=30, blank=True, null=True)
    company_name = models.CharField('Название компании', max_length=50)
    description = models.TextField('Описание компании')
    contacts = models.TextField('Контакты компании')
    address = models.TextField('Адрес проживания пользователя', null=True, blank=True)
    avatar = models.ImageField('Аватар пользователя', upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь работодатель'
        verbose_name_plural = 'Пользователи работодатели'
        db_table = 'employer_users'
