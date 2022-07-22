import mailbox
from django.shortcuts import render

from dangky.models import NguoiDung

# Create your views here.

def dangky(request):
    return render(request,'dangky.html')

def trangchu(request):
    return render(request,'trangchu.html')

def xuly_dangky(request):
    ten = request.GET.get('ten')
    email = request.GET.get('email')
    mk = request.GET.get('matkhau')

    # if (len(ten)>10 and ('@' in email)):
    if (len(ten)<10):
        return render(request,'Error.html')
    else:
        dulieu = NguoiDung(
            ten_dang_nhap = ten,
            email = email,
            mat_khau = mk,
        )
        dulieu.save()
        return render(request,'dangnhap.html')
    # print(ten)