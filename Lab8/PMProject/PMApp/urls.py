from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('',views.base, name='base'),
    path('form',views.form,name='form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)