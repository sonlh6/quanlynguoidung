from django.contrib import admin
from django.urls import path
from nhanvien import views
urlpatterns = [
    path('', views.nhanvien),
    path('xuly_nhanvien/',views.xuly_nhanvien, name="xuly_nhanvien"),
]