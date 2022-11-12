from django.db import models


# python manage.py makemigrations
# python manage.py migrate


class HomeWork(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0)
    views_count = models.IntegerField()
    status = models.ForeignKey("HomeWorkStatus", default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class HomeWorkStatus(models.Model):
    name = models.CharField(max_length=100)



