from django.urls import path
import FirstApp.views


urlpatterns = [
    path('', FirstApp.views.form_example)
]