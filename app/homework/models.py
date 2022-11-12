from django.db import models

# Create your models here.


class HomeWork(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
