from django.contrib import admin
from .models import Todolist

# Register your models here.

@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_completed')
    list_filter = ('is_completed',)
    search_fields = ('title',)
    list_per_page = 5
    list_editablel = ('is_completed',)
# admin.site.register(Todolist,TodolistAdmin)
