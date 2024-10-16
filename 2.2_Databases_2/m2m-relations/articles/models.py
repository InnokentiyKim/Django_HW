from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='Тег')
    articles = models.ManyToManyField('Article', related_name='tags', through='Scope')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='scopes', verbose_name='Тег')
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['-is_main', 'tag__title']
