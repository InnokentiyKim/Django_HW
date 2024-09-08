from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                return form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'text')
    list_filter = ('published_at', )
    inlines = (ScopeInline, )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = (ScopeInline, )
