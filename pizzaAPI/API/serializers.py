from rest_framework import serializers

from .models import PizzaType, PizzaSize, PizzaTopping


class PizzaToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaTopping
        fields = '__all__'

class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = '__all__'

class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'
        read_only_fields = ('pizza_size_category', 'pizza_topping_category')
        depth = 1
