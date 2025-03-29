from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImagesInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_image',]
    extra = 0

    def get_image(self, obj):
        return format_html(
            '<img src="{}" style="max-height:200px; max-width:200px;" />',
            obj.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title',]
    inlines = [ImagesInline]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']
