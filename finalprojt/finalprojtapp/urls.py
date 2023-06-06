from django.contrib import admin
from django.urls import path
from .import views
app_name ='finalprojtapp'

urlpatterns = [path('',views.demo,name='demo'),
               path('login',views.login,name='login'),
               path('register',views.register,name='register'),
               path('logout', views.logout, name='logout'),
               path('new', views.new, name='new'),
               path('getdata/',views.getdata,name="getdata"),
               path('regform',views.regform,name="regform"),
               ]