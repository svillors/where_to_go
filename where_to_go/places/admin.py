from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html


class ImagesInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_image',]

    def get_image(self, obj):
        return format_html(
            '<img src="{}" width="{}" height="{}" style="max-height:200px; height:auto; width:auto;" />',
            obj.image.url,
            obj.image.width,
            obj.image.height
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
