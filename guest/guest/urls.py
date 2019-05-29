"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from sign import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('accounts/login/', views.index),
    path('', views.index),
    path('search_name/', views.search_name),
    path('guest_manage/', views.guest_manage),
    path('search_guest/', views.search_guest),
    path('search_phone/', views.search_phone),
    path('sign_index/<event_id>/', views.sign_index),
    path('sign_index_action/<event_id>/', views.sign_index_action),
    path('logout/', views.logout),
    path('api/', include('sign.urls', namespace="sign")),
]
