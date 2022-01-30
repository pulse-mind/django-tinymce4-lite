"""test_tinymce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import include
    2. Import the re_path : from django.urls import re_path
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from .views import TestCreateView, TestDisplayView


urlpatterns = [
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^admin/filebrowser/', site.urls),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^content/(?P<pk>\d+)/$', TestDisplayView.as_view(), name='display'),
    re_path(r'^$', TestCreateView.as_view(), name='create')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
