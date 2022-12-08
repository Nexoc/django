# Generated by Django 4.1.2 on 2022-11-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_homework_created_at_homework_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='homework',
            name='views_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]