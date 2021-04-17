"""awadh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from . import file

urlpatterns = [
    path('admin/', admin.site.urls),
    # print("okk report")
    path('', file.start,name="index"),
    path('programming/', file.programming ,name="programming"),
    path('class9/', file.class9 ,name="class9"),
    path('class8/', file.class8 ,name="class8"),
    path('class10/', file.class10 ,name="class10"),
    path('contact/', file.contact ,name="contact"),
    path('login/', include('registrarion.urls'), name='registeration'),
    path('programming/courses/basic/basic2/', file.basic ,name="basic"),
    path('programming/courses/cc++/cc++/', file.ccpp ,name="cc++"),
    path('programming/courses/python/python/', file.python ,name="python"),
    path('programming/courses/webdevlopment/webdevlopment/', file.webdevlopment ,name="webdevlopment"),
    path('programming/courses/django/django/', file.django ,name="django"),
    path('programming/courses/androidstudio/androidstudio/', file.androidstudio ,name="androidstudio"),
    path('booklist', file.booklist ,name="booklist"),
    path('live', include('livesession.urls') ,name="live"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

