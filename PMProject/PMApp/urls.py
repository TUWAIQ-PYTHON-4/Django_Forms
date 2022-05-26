from django.urls import path
from django.contrib import admin
import PMApp.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PMApp.views.admin_object),
    path('form/',PMApp.views.form)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)