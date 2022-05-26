from django.contrib import admin

from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'completion_time')
    date_hierarchy = 'completion_time'


admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_filter = ('completed',)
    search_fields = ['project']


admin.site.register(Task, TaskAdmin)
