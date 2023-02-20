
from django.contrib import admin
from django.urls import path,re_path
from info.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
   path('ckeditor/', include('ckeditor_uploader.urls')),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)