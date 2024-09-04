# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

    class Meta:
        verbose_name = u'Книга'
        ordering = ['pub_date']
        indexes = [
            models.Index(fields=['pub_date']),
        ]
