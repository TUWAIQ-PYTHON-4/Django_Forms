from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('form-example/', views.form_example, name = 'form_example')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
