"""
URL configuration for VideoCollect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Videos import views as video_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',video_views.index,name='index'),
    path('dictionary/list',video_views.dictionarylist,name='dictionary'),
    path('dictionary/all',video_views.dictionaryview,name='dictionaryall'),
    path('dictionary/update',video_views.DictionaryUpdate.as_view(),name='dictionaryupdate'),
    path('sign/video/list',video_views.SignVideolist.as_view(),name='sign video'),
    path('sign/upload/', video_views.SignVideoUpload.as_view(), name='signvideo-upload'),
    path('search/<str:query>/', video_views.SearchAPIView.as_view(), name='search-api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
