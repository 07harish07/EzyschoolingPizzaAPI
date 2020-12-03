from django.contrib import admin
from .models import PizzaType, PizzaSize, PizzaTopping

admin.site.register(PizzaType)
admin.site.register(PizzaSize)
admin.site.register(PizzaTopping)
