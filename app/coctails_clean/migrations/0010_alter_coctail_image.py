# Generated by Django 4.1.2 on 2022-12-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coctails_clean', '0009_alter_coctail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coctail',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
