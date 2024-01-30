"""
URL configuration for taxiehai project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:pk>/', views.product_info, name='product_info'),
    path('catalog/', views.catalog, name='catalog'),
    path('search/', views.search, name='search'),
    path('<int:pk>/newr/', views.newreview, name='product_newreview'),
    path('<int:pk>/o/', views.order_n, name='order_n'),
    path('<int:pk>/o/add/', views.order_add, name='order_add'),
    # path('<int:pk>/o/add', views.order_n, name='order_add'),
    # path('admin/', admin.site.urls),
]
