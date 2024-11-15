# Generated by Django 5.1.3 on 2024-11-15 10:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_remove_company_date_container_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Введите дату', verbose_name='Дата'),
        ),
    ]