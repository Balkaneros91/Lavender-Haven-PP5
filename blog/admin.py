from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
