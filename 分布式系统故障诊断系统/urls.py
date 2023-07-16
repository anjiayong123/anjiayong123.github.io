"""分布式系统故障诊断系统 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from User.views import register,login

#admin.site.login_template = 'admin/login.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/', include('User.urls')),
    path('register/',register),
    path('login/',login),
    path('test_upload/',views.test_upload),
    path('xd/test_upload/',views.my_view),
    path('xd/',views.xd),
    path('bg/jj/',views.my_view_01),
    path('jj/',views.jj),
    path('upload_app/', include('upload_app.urls')),
    path('jj/upload_app/model/',views.my_view_02),
    path('guzhang/',views.gz),
    path('xd/guzhang/',views.my_view_03),
    path('guzhang/test_upload/',views.my_view_04),
    path('db/',views.db),
    path('jj/db/',views.my_view_05),
    path('peie/',views.peie),
    path('gr/',views.gr),
    path("",views.redic),
    path('upload', views.upload_file, name='upload'),
    # path('denglu/',views.denglu),
    path('xz/upload_app/model/',views.rr),
    path('houtai/',views.houtai),
    path('bg/',views.bg),
    path('fff/', views.fff),
    path('ks/', views.ks),
    path('xz/',views.xz),
    path('yx/',views.yx),
    path('fff/yx/',views.re),



]
#media的路由需要手动配置
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
