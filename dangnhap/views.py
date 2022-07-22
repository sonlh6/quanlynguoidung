from urllib import request
from django.shortcuts import get_object_or_404, render
from dangky.models import NguoiDung
from nhanvien import *
# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')

    thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten,mat_khau=mk)

    danh_sach = NguoiDung.objects.all()

    context = {
        'ds_nguoidung': danh_sach
    }
    #tương đương với câu lệnh select * from ... where ...
    if (thongtin.exists()):
        # print(context)
        return render(request,'danhsach.html',context)
    else:
        return render (request,'loi.html')

def chi_tiet(request, nguoidung_id):
    nguoi_dung = get_object_or_404(NguoiDung,pk = nguoidung_id)
    return render(request,'chitiet.html',{'nd':nguoi_dung})

def xuly_capnhatnv(request):
    ten = request.GET.get('ten')
    email = request.GET.get('email')
    mat_khau = request.GET.get('matkhau')
    id_nv = request.GET.get('id_nv')
    
    NguoiDung.objects.filter(id=id_nv).update(
        ten_dang_nhap = ten,
        email = email,
        mat_khau = mat_khau
    )
    danh_sachnd = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sachnd
    }
    return render(request,'danhsach.html',context)


def xoa_nguoidung(request,nguoidung_id):
    dulieu = get_object_or_404(NguoiDung, pk = nguoidung_id)
    try:
        dulieu.delete()
    except:
        print("Xoá bị lỗi")
    danh_sachnd = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sachnd
    }
    return render(request,'danhsach.html',context)