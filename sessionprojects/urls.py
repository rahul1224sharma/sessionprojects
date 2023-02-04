"""sessionprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from MyApps1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',views.set_cookie),
    path('test/',views.check_view),
    path('count/',views.count),
    path('home/',views.home_view),
    path('second/',views.date_time_view),
    path('result/',views.result_view),
    path('name/',views.name_view),
    path('age/',views.age_view),
    path('parent/',views.parent_view),
    path('result1/',views.result1),
    path('home1/',views.index1),
    path('additem/',views.additem),
    path('displayitem/',views.displayitem),
    path('count/',views.page),
    	#Session-Application-2
    path('name1/', views.name1),
    path('age2/', views.age1),
    path('parent2/', views.pname2),
    path('results/', views.result2),
    path('additem2/',views.additem),
    path('display/',views.dis),
]
