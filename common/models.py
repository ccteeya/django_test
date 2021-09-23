from django.db import models

# Create your models here.

class Custormer(models.Model):

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    qq = models.CharField(max_length=30, null=True, blank=True)


#register model to django
from django.contrib import admin
admin.site.register(Custormer)