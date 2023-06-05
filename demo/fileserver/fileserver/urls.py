# from django.contrib import admin
# from django.urls import path, include
from fileupload import views as fileupload_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', fileupload_views.home, name='home'),
    
# ]


# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fileupload_views.home, name='home'),
    path('fileupload/', include('fileupload.urls', namespace='fileupload')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
