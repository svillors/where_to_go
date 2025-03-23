from django.contrib import admin
from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
