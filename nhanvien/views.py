from django.shortcuts import render
from nhanvien.models import NhanVien
# Create your views here.
def nhanvien(request):
    return render(request,'nhanvien.html')

def xuly_nhanvien(request):
    ten = request.GET.get('nv')
    chucvu = request.GET.get('chucvu')
    namsinh = request.GET.get('namsinh')

    # if (len(ten)>10 and ('@' in email)):
    if (len(ten)<10):
        return render(request,'Error.html')
    else:
        dulieu = NhanVien(
            ho_ten = ten,
            chuc_vu = chucvu,
            nam_sinh = namsinh,
        )
        dulieu.save()
        return render(request,'thanhcong.html')