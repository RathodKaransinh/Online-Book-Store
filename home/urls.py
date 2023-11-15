"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('orders', views.orders, name='orders'),
    path('order/<str:label>', views.order, name='order'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('register',views.registerUser, name="register"),
    path('add',views.addProduct, name="add"),
]