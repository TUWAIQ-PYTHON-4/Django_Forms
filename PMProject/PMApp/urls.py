from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.project_object, name= 'project_object'),
    path('tasks/', views.project_tasks_object, name= 'project_tasks_object'),
    path('taskform/', views.task_form, name= 'task_form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)