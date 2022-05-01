"""cancer URL Configuration

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

from django.urls import path
from . import front_connect
from django.conf import settings
from django.contrib import admin

from django.conf.urls.static import static

urlpatterns = [
    path('',front_connect.home),
    path('admin/', admin.site.urls),
    path('home/',front_connect.home,name='home'),
    path('home2/',front_connect.home2,name='home2'),
    path('home3/',front_connect.home3,name='home3'),
    path('testing/',front_connect.testing,name='home4'),
]