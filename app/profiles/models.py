from django.db import models

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    # birthday = models.DateField()
