from django.db import models

from users.models import SchoolUser, EmployerUser

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class AdCategory(models.Model):
    """Категория объявления"""
    name = models.CharField('Название категории работника', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ads_category'
        verbose_name = 'Категория объявления'
        verbose_name_plural = 'Категории объявлений'


class Ad(models.Model):
    """Объявление"""
    owner = models.ForeignKey(EmployerUser, on_delete=models.CASCADE)
    users = models.ManyToManyField(SchoolUser)
    limit = models.IntegerField(default=1, verbose_name='Количество')
    payment = models.IntegerField('Оплата за час работы RUB')
    title = models.CharField('Загаловок объявления', max_length=100)
    description = models.TextField('Описание объявления')
    category = models.ForeignKey(AdCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ads'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class AdSchedule(models.Model):
    """Расписание объявления"""
    start = models.TimeField('Время начала работы')
    stop = models.TimeField('Время окончания работы')
    week_day = models.IntegerField(choices=DAYS_OF_WEEK)
    ad = models.ForeignKey(Ad, models.CASCADE)

    def __str__(self):
        return f"{self.start}:{self.stop} {self.week_day}"

    class Meta:
        db_table = 'ads_schedule'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class AdPhoto(models.Model):
    """Фотография объявления"""
    photo = models.ImageField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name

    class Meta:
        db_table = 'ads_photo'
        verbose_name = 'Фотография объявления'
        verbose_name_plural = 'Фотографии объявлений'
