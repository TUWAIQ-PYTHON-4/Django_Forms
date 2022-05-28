from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.base, name = 'pmp'),
    path('project/', views.project, name = 'pro'),
    path('task/', views.task, name = 'tas'),
    path('addproject/', views.AddProject, name = 'add'),
    #path('projects/<int:pk>/', views.AddProject, name = 'project_edit'),
    #path('projects/new/', views.AddProject, name = 'project_create')

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


