# Generated by Django 3.2.15 on 2022-08-26 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20220826_1944'),
        ('users', '0007_auto_20220826_1944'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployerUser',
        ),
        migrations.DeleteModel(
            name='SchoolUser',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
