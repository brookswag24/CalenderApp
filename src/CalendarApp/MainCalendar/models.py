from django.db import models

# Create your models here.


class SaintDay(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    discription = models.CharField(max_length=150)


class FastDays(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    discription = models.CharField(max_length=150)
