from django.db import models

# python manage.py makemigrations coctails
# python manage.py migrate


class Coctail(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    alcohol = models.ForeignKey("Alco", on_delete=models.CASCADE)
    season = models.ForeignKey("Season", on_delete=models.CASCADE)
    type_of_drink = models.ForeignKey("Type_Of_Drink", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title"]


class Alco(models.Model):
    alcoholic = models.CharField(max_length=100)

    def __str__(self):
        return self.alcoholic


class Season(models.Model):
    season = models.CharField(max_length=100)

    def __str__(self):
        return self.season


class Type_Of_Drink(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
