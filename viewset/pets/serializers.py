from rest_framework import serializers
from .models import Pets, Order


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'