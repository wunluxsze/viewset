from django.contrib import admin
from .models import Pets, Order, Category, Type, Status
# Register your models here.
admin.site.register(Pets),
admin.site.register(Order),
admin.site.register(Category),
admin.site.register(Type),
admin.site.register(Status)