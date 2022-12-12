from django.contrib import admin
from django.contrib import admin
from .models import Coctail, Alco, Season, Type_Of_Drink

# Register your models here:
admin.site.register(Coctail)
admin.site.register(Alco)
admin.site.register(Season)
admin.site.register(Type_Of_Drink)
