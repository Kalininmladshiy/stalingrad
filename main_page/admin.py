from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ['picture', 'get_preview']
    extra = 1

    def get_preview(self, img):
        return format_html(
            '<img src="{url}" height={height} />',
            url=img.picture.url,
            height=200,
         )
    get_preview.short_description = u"Превью изображения"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description_short')
    inlines = [PlaceImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
