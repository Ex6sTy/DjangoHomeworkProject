from django.contrib import admin
from .models import BlogPost
from django.utils.html import format_html


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'is_published', 'views', 'created_at', 'preview_image')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('views', 'created_at', 'preview_tag')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'is_published', 'preview', 'preview_tag')
        }),
        ('Дополнительно', {
            'fields': ('views', 'created_at'),
        }),
    )

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = 'Кратко'

    def preview_image(self, obj):
        if obj.preview:
            return format_html('<img src="{}" width="80" style="border-radius: 4px;" />', obj.preview.url)
        return '—'
    preview_image.short_description = 'Превью'

    def preview_tag(self, obj):
        if obj.preview:
            return format_html('<img src="{}" width="200" style="border-radius: 6px;" />', obj.preview.url)
        return "Нет изображения"
    preview_tag.short_description = "Изображение"

