from django.contrib import admin
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'completion_time')
    date_hierarchy='creation_time'


admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_filter = ('project',)
    search_fields = ['title', ]


admin.site.register(Task, TaskAdmin)
