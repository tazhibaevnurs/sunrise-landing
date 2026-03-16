"""
Регистрация моделей в админке Django.
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import Application, SiteImage, FAQItem, Story, ContactInfo


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'application_type', 'created_at', 'is_processed')
    list_filter = ('application_type', 'is_processed', 'created_at')
    search_fields = ('name', 'phone')
    list_editable = ('is_processed',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'get_preview', 'alt', 'has_image', 'has_url_override')
    list_editable = ('alt',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug',)
        return ()

    def get_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:60px; max-width:120px; object-fit:contain;">',
                obj.image.url,
            )
        return '—'
    get_preview.short_description = 'Превью'

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Файл'

    def has_url_override(self, obj):
        return bool(obj.url_override)
    has_url_override.boolean = True
    has_url_override.short_description = 'Ссылка'


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address_1', 'address_2')
    list_display_links = ('phone',)

    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'tagline_short', 'order', 'get_preview')
    list_editable = ('order',)
    list_filter = ('role',)
    search_fields = ('name', 'tagline', 'testimonial')

    def tagline_short(self, obj):
        return (obj.tagline[:50] + '…') if len(obj.tagline) > 50 else obj.tagline
    tagline_short.short_description = 'Цитата'

    def get_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-height:40px; max-width:40px; border-radius:50%%; object-fit:cover;">',
                obj.photo.url,
            )
        return '—'
    get_preview.short_description = 'Фото'


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question_short', 'order')
    list_editable = ('order',)
    ordering = ('order',)

    def question_short(self, obj):
        return obj.question[:80] + ('…' if len(obj.question) > 80 else '')
    question_short.short_description = 'Вопрос'
