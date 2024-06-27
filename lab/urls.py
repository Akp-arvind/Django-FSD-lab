"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ap1.views import Current_datetime 
from ap1.views import four_hours_ahead
from ap1.views import four_hours_before, display_string
from ap2.views import showlist  
from ap3.views import aboutus,home,contactus
from ap4.views import reg,course_search

# prog 6
admin.site.site_header = "Registration System"
admin.site.site_title = "Tables for Registration"
admin.site.index_title = "Welcome to Registration System"

# add cdt here itself
urlpatterns = [
    path('admin/', admin.site.urls), # no = req after path, used in prog 6
    path('cdt/', Current_datetime),
    path('fha/', four_hours_ahead),
    path('fhb/', four_hours_before),
    path('display_string|<str:s>', display_string),
    # / works too in place of pipe above
    path('showlist/', showlist), # ap2
    path('aboutus/', aboutus),
    path('home/', home),
    path('contactus/', contactus),
    path('reg/', reg),
    path('course_search/', course_search),
]     