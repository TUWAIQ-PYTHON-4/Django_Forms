
from django.contrib import admin
from .models import  Project ,Task


class projectAdmin(admin.ModelAdmin):
     list_display = ['name','creation_time']
     date_hierarchy = 'creation_time'
     search_fields=['name']


class taskAdmin(admin.ModelAdmin):
   list_display = ['title']
   list_filter = ('description',)



admin.site.register(Project,projectAdmin)
admin.site.register(Task,taskAdmin)
