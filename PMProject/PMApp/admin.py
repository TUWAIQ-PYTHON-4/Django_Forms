from django.contrib import admin
from .models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['name']
    date_hierarchy = 'creation_time'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('description',)
    search_fields = ['title']
    #date_hierarchy = 'time_estimate'

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)

