from django.contrib import admin
from django.contrib import admin

from .models import Project, Task


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'completion_time')
    list_filter = ('name',)
    date_hierarchy = ('creation_time')
    search_fields = ('name',)


admin.site.register(Task)
admin.site.register(Project, ProjectAdmin)
