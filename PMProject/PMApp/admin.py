from django.contrib import admin

# Register your models here.

from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "creation_time",)
    list_filter = ('name','completion_time',)
    date_hierarchy = 'creation_time'
    search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)
    list_filter = ('title','completed',)
    search_fields = ('title',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
