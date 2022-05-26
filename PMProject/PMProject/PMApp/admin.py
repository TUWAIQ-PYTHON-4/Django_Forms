from django.contrib import admin
from .models import Project
from .models import Task
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','creation_time','completion_time')
    date_hierarchy = ('completion_time')
    #


class TaslAdmin(admin.ModelAdmin):
    list_display = ('title','time_estimation')
    list_filter = ('project',)
    search_fields = ('title',)

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaslAdmin)