from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели в интерфейсе админки."""

    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели в интерфейсе админки."""

    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
