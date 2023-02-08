from django.contrib import admin
from .models import *

# Добавлене дополнительных полей в админ панели сайта

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create',)
    list_display_links = ('id','title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',) # Список полей по которым будет сортировка
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Регистрация нашего приложения в админ панели сайта
admin.site.register(Post, PostAdmin)


