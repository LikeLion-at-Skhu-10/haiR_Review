"""haireview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
import main.views
import free.views
import review.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name = 'main'),
    path('f_write/', free.views.f_write, name = 'f_write'),
    path('f_list/', free.views.f_list, name='f_list'),
    path('f_detail/<str:id>/', free.views.f_detail, name='f_detail'),
    path('f_edit/<str:id>/', free.views.f_edit, name='f_edit'),
    path('f_delete/<str:id>/', free.views.f_delete, name='f_delete'),
    path('f_hashtag/', free.views.f_hashtag, name='f_hashtag'),
    path('r_write/', review.views.r_write, name='r_write'),
    path('r_list/', review.views.r_list, name='r_list'),
    path('r_detail/<str:id>/', review.views.r_detail, name='r_detail'),
    path('r_edit/<str:id>/', review.views.r_edit, name='r_edit'),
    path('delete/<str:id>/', review.views.delete, name='delete'),
    path('r_hashtag/', review.views.r_hashtag, name='r_hashtag'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
