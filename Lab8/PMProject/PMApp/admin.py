from django.contrib import admin
from .models import Project,Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'completion_time')
    date_hierarchy = 'creation_time'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_estimation')
    list_filter = ('time_estimation',)
    search_fields = ['title']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
