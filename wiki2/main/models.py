import os
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Создание статей
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи") # Заголовок статьи
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = RichTextUploadingField(verbose_name="") # Пост. Значение false говорит о том, что поле не может быть пустым.
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank = True, null = True)
    file = models.FileField(upload_to='file/%Y-%m-%d/', blank=True, null = True, verbose_name="")

# Делаем имя файлам
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myurl', kwargs={'post_slug': self.slug}) # В админ панели появится кнопка смотреть на сайте

    class Meta:
        verbose_name = 'Публикации' # В админ панели, класс получит название как "публикции"
        verbose_name_plural = 'Публикации' # Используем команду для множественнго числа
        ordering = ['time_create', 'title']