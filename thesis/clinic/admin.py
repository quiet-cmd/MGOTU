from django import forms
from django.contrib import admin
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'cat')
    search_fields = ['name', 'code', 'cat__name']


@admin.register(CategoryServices)
class CategoryServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(ClinicDocuments)
class ClinicDocumentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'cat')
    search_fields = ['name', 'cat__name']


@admin.register(CategoryClinicDocuments)
class CategoryClinicDocumentsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'specialization', 'experience')
    search_fields = ['name', 'position', 'specialization']


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('title', 'text', 'cat')
    search_fields = ['title', 'cat__name']


@admin.register(CategoryArticle)
class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
