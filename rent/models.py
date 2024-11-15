from django.utils import timezone

from django.db import models
from django.db.models import CASCADE

NULLABLE = {'null':True, 'blank':True}

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя/Название', help_text='Введиет название компании или имя ч/л')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона', help_text='Введите номер телефона для связи')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Container(models.Model):
    class AgeChoices(models.TextChoices):
        UNDER_5_RU = 'under_5_ru', 'Моложе 5 лет, РФ'
        UNDER_5_CH = 'under_5_ch', 'Моложе 5 лет, Китай'
        OVER_5_RU = 'over_5_ru', 'Старше 5 лет РФ'
        OVER_5_CH = 'over_5_ch', 'Старше 5 лет Китай'

    name = models.CharField(max_length=50, verbose_name='Наименование баллона', help_text='Введите наименование баллона')
    company = models.ForeignKey(Company, on_delete=CASCADE, verbose_name='Клиент')
    age_group = models.CharField(max_length=10, choices=AgeChoices.choices, verbose_name='Вид тары')
    count_shipped = models.IntegerField(**NULLABLE, verbose_name='Количество отгружено', help_text='Введите количество отгруженых баллонов')
    count_taken = models.IntegerField(**NULLABLE, verbose_name='Количество принято', help_text='Введите количество принятых баллонов')
    duration = models.CharField(max_length=255, **NULLABLE, verbose_name='Срок аренды', help_text='Предположительный срок арены')
    date = models.DateField(default=timezone.now, verbose_name='Дата', help_text='Введите дату')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Баллон'
        verbose_name_plural = 'Баллоны'

    class Nomenclature(models.Model):
        name = models.CharField(max_length=255, verbose_name='Наименование баллона')