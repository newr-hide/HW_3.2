from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Badge

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:

            tmp_data = form.cleaned_data
            if 'is_main' in tmp_data:  # проверка существования ключа
                if tmp_data['is_main'] == True:
                    count += 1
            else:
                continue
        if count > 1:
            raise ValidationError('Должен быть только один элемент с галочкой Основной')
        elif count < 1:
            raise ValidationError('Должен быть хотя бы один элемент с галочкой Основной')
        else:
            return super().clean()



class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    pass

