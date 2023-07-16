from django.contrib import admin
from .models import Content
# Register your models here.
class CommentManager(admin.ModelAdmin):
    list_display = ['title','data']
admin.site.register(Content,CommentManager)