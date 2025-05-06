from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80"/>', obj.image.url)
        return "—"
    preview.short_description = "Превью"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner', 'status', 'image')
    list_filter = ('category', 'status')
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'image', 'category', 'price', 'status', 'owner')


    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:4px;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Изображение"
