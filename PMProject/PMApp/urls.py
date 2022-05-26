from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'PMApp'

urlpatterns = [
                  path('', views.form_example, name='form_example'),
                  # path('about/', views.about, name='about'),
                  # path('PMApp/', views.form_example)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
