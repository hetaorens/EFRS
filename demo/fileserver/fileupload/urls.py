from django.urls import path
from . import views

app_name = 'fileupload'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('check/', views.check_file, name='check_file'),
]
