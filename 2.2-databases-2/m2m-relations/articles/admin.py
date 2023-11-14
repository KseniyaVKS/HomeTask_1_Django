from django.contrib import admin
from django.core.exceptions import ValidationError
# from django.forms import BaseInlineFormSet
from django import forms

from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            is_main = form.cleaned_data['is_main']
            if is_main:
                count += 1
            if count == 0:
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
                raise ValidationError('Укажите главный раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['published_at']
    inlines = [ArticleScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']