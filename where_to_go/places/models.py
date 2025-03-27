from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = tinymce_models.HTMLField('Длинное опичание', blank=True)
    longitude = models.DecimalField('Долгота', max_digits=20, decimal_places=17)
    latitude = models.DecimalField('Широта', max_digits=20, decimal_places=17)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Место на карте"
    )
    image = models.ImageField('Картинка')
    position = models.PositiveIntegerField('Позиция', default=1, db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f' Image number {self.position} for {self.place.title}'
