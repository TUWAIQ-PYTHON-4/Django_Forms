from django.contrib import admin
from .models import Task, Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name','creation_time','completion_time')
    search_fields = ('name',)
    date_hierarchy = ('creation_time')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_estimate','completed')
    list_filter = ('title',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task,TaskAdmin)



