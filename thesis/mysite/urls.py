from django.contrib import admin
from django.urls import path, include

from clinic.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('quiet-cmd/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='main'),
    path('services', services, name='services'),
    path('doctors', doctors, name='doctors'),
    path('doctor/<int:doctor_id>', doctor, name='doctor'),
    path('documents', documents, name='documents'),
    path('articles', articles, name='articles'),
    path('article/<int:article_id>', article, name='article')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
