from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *  

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(AtCategory)

class ProductImageStackedInline(admin.TabularInline):

    model = ImageProduct
    extra = 1


class ProductAttributeStackedInline(admin.TabularInline):

    model = AttributeProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'decription', 'category', 'get_image')
    list_display_links = ('id', 'name',)
    list_filter = ('category',)
    search_fields = ('name', 'decription',)
    readonly_fields = ('created_at', 'updated_at', 'get_big_image',)
    inlines = [ProductAttributeStackedInline, ProductImageStackedInline]

    @admin.display(description='Изображение')
    def get_image(self, item):
        img = item.image.first() if hasattr(item.image, 'first') else item.image  
        if img and hasattr(img, 'url'):
            return mark_safe(f'<img src="{img.url}" width="150px">')
        return '-'

    @admin.display(description='Изображение')
    def get_big_image(self, item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="100%">')
        return '-'


# Register your models here.
