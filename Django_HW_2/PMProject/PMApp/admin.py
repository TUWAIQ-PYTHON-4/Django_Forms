from django.contrib import admin
from .models import Project, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('project',)
    search_fields=('title',)

class projectAdmin(admin.ModelAdmin):
    date_hierarchy=('creation_time')



admin.site.register(Task,TaskAdmin)
admin.site.register(Project,projectAdmin)
