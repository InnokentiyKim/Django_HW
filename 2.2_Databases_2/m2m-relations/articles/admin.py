from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tags += 1
        if main_tags == 0:
            raise ValidationError('Один из тегов должен быть основным')
        elif main_tags > 1:
            raise ValidationError('Основной тег может быть только один')
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
