# Generated by Django 4.1.2 on 2022-12-22 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coctails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coctail',
            name='price',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
    ]
