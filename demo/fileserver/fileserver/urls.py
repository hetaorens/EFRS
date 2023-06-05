from django.contrib import admin
from django.urls import path, include
from fileupload import views as fileupload_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fileupload_views.home, name='home'),
    path('fileupload/', include('fileupload.urls', namespace='fileupload')),
]
