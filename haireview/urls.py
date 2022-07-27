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
from django.contrib import admin
from django.urls import path
import QnA.views , main.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , main.views.main, name = 'main'),
    path('q_write/' , QnA.views.q_write, name = 'q_write'),
    path('q_list/' , QnA.views.q_list, name = 'q_list'),
    path('q_detail/<str:id>/' , QnA.views.q_detail, name = 'q_detail'),
    path('q_edit/<str:id>/' , QnA.views.q_edit, name = 'q_edit'),
    path('q_delete/<str:id>/' , QnA.views.q_delete, name = 'q_delete'),                               
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
