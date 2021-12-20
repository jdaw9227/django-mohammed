from django.db import models

# Create your models here.


class Restaurants(models.Model):
    type = models.TextField(max_length=200)  # max_length can be more than 255
    code = models.CharField(max_length=200)  # CharField has max_length of 255
