from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Project,Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time','completion_time')
    date_hierarchy = 'creation_time'

class PAdmin(admin.ModelAdmin):
    list_filter = ('project',)
    search_fields = ['title', ]

admin.site.register(Project,ProjectAdmin)

admin.site.register(Task,PAdmin )