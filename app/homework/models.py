from django.db import models


# python manage.py makemigrations
# python manage.py migrate

# to add
# python manage.py shell
# from homework.models import HomeWork
# my_first = HomeWork(title='first time')
# my_first.save()

# to add status as FK
# status = HomeWorkStatus(name='it works')
# status.save()
# from homework.models import HomeWork
# adv = HomeWork.objects.first()
# adv.status = status
# adv.save()
# adv.status.name


class HomeWork(models.Model):
    title = models.CharField(max_length=30, db_index=True)  # index -> speed search
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0)
    views_count = models.IntegerField(default=0)
    status = models.ForeignKey("HomeWorkStatus", default=None, null=True, on_delete=models.CASCADE,
                               related_name="homework", verbose_name="status")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "hausaufgabe"  # rename DB
        ordering = ['title']  # order by title


class HomeWorkStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
