from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Класс отображения в админке пользователей(модель CustomUser)"""
    list_display = 'name', 'id', 'random_id', 'preview'
    search_fields = 'name', 'id', 'random_id'
    search_help_text = 'Поиск по имени пользователя, id пользователя и cгенерированного id'
    list_filter = "name",

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50">')
    preview.short_description = 'Аватар'