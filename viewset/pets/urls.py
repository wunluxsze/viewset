from django.contrib import admin
from django.urls import path, include
from .views import Petviewset, Orderviewset

urlpatterns = [
    path('pets', Petviewset.as_view({'get': 'list', 'post': 'create'})),
    path('pet/<int:pk>', Petviewset.as_view({'get':'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('orders', Orderviewset.as_view({'get': 'list', 'post': 'create'})),
    path('order/<int:pk>', Orderviewset.as_view({'get':'retrieve', 'delete': 'destroy', 'put': 'update'})),
]