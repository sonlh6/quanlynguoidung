from django.contrib import admin
from django.urls import path
from dangnhap import views
urlpatterns = [
    path('', views.dangnhap),
    path('xuly_dangnhap/',views.xuly_dangnhap, name="xuly_dangnhap"),
    path('chitiet/<int:nguoidung_id>/',views.chi_tiet,name="chi_tiet"),
    path('xuly_capnhatnv',views.xuly_capnhatnv,name="xuly_capnhatnv"),
    path('xoa/<int:nguoidung_id>/',views.xoa_nguoidung,name="xoa_nguoidung"),
]
