from django.db import models


class PizzaTopping(models.Model):
    pizza_topping = models.CharField(max_length=30, null=True)


    def __str__(self):
        return f"{self.pizza_topping}"

class PizzaSize(models.Model):
    pizza_size = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.pizza_size}"


class PizzaType(models.Model):
    pizza_type = models.CharField(max_length=30, null=True)
    pizza_size_category = models.ForeignKey(PizzaSize, related_name='pizza_size_category', on_delete=models.SET_NULL, null=True)
    pizza_topping_category = models.ForeignKey(PizzaTopping, related_name='pizza_topping_category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pizza_type}"
