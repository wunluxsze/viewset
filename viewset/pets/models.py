from django.db import models
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=200)


class Type(models.Model):
    type = models.CharField(max_length=200)


class Status(models.Model):
    status = models.CharField(max_length=200)


class Pets(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Order(models.Model):

    STATUS = [
        ('выполнен', 'выполнен'),
        ('обработан', 'обработан'),
        ('размещен', 'размещен'),
    ]

    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    count = models.IntegerField()
    data = models.DateField()
    status = models.CharField(max_length=200, choices=STATUS)
    iscompleted = models.BooleanField(default=False)
