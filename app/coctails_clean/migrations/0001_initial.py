# Generated by Django 4.1.2 on 2022-12-26 11:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcoholic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Of_Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coctail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('alcohol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coctails_clean.alco')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coctails_clean.season')),
                ('type_of_drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coctails_clean.type_of_drink')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
