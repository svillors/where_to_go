from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    title_short = models.CharField(max_length=70)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.DecimalField(max_digits=20, decimal_places=17)
    latitude = models.DecimalField(max_digits=20, decimal_places=17)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f' Image number {self.position} for {self.place.title}'
