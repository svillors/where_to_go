from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline


class ImagesInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_image',]
    extra = 0

    def get_image(self, obj):
        return format_html(
            '<img src="{}" width="{}" height="{}" style="max-height:200px; height:auto; width:auto;" />',
            obj.image.url,
            obj.image.width,
            obj.image.height
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title',]
    inlines = [ImagesInline]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
