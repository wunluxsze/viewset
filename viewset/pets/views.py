from django.shortcuts import render
from rest_framework import  viewsets
from .models import Pets, Order
from .serializers import PetSerializer, OrderSerializer


class Petviewset(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetSerializer


class Orderviewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
