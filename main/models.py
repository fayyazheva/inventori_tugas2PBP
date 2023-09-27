from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
# Product adalah nama model yang kamu definisikan.
# nama, tanggal_tambah, harga, dan deskripsi adalah atribut atau field pada model. Setiap field memiliki tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField
# user = kode diatas berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user. Lebih lanjutnya terkait ForeignKey akan dipelajari pada mata kuliah Basis Data. 

