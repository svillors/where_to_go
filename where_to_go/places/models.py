from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.DecimalField(max_digits=17, decimal_places=14)
    latitude = models.DecimalField(max_digits=17, decimal_places=14)
