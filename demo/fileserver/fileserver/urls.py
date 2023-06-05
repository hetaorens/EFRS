from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
]

from django.contrib import admin
from django.urls import path
from fileupload import views as fileupload_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fileupload_views.home, name='home'),
    path('fileupload/', include('fileupload.urls', namespace='fileupload')),
]
