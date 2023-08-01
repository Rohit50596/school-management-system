"""schoolmanagement URL Configuration

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),
    path('home/',home),
    path('personalinfo/',personalinfo),
    path('schoolinfo/',schoolinfo),
    path('updatepinfo/',updatepinfo),
    path('updatesinfo/',updatesinfo),
    path('up/',up),
    path('us/',us),
    path('deletestudent/',deletestudent),
    path('student/',student),
    path('clearfee/',clearfee),
    path('balancecheck/',balancecheck),
    path('transactions/',transactions),
    path('allstudents/',allstudents),
    path('addemployee/',addemployee),
    path('alltransactions/',alltransactions),
    path('logout/',logout),
]
