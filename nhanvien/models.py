import email
from django.db import models

# Create your models here

class NhanVien(models.Model):
    ho_ten = models.CharField(max_length=100)
    chuc_vu = models.CharField(max_length=100)
    nam_sinh = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.ten_dang_nhap