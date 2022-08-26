# Generated by Django 3.2.15 on 2022-08-16 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_alter_schooluser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooluser',
            name='description',
            field=models.TextField(default='', verbose_name='Описание пользователя'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='EmployerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия пользователя')),
                ('second_name',
                 models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество пользователя')),
                ('company_name', models.CharField(max_length=50, verbose_name='Название компании')),
                ('description', models.TextField(verbose_name='Описание компании')),
                ('contacts', models.TextField(verbose_name='Контакты компании')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес проживания пользователя')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=users.models.upload_to,
                                             verbose_name='Аватар пользователя')),
                (
                    'user',
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь работодатель',
                'verbose_name_plural': 'Пользователи работодатели',
                'db_table': 'employer_users',
            },
        ),
    ]
