from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

# models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
# Product adalah nama model yang kamu definisikan.
# nama, tanggal_tambah, harga, dan deskripsi adalah atribut atau field pada model. Setiap field memiliki tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField

