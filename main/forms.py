from django.forms import ModelForm
from main.models import Product
from django import forms


class ProductForm(ModelForm):
    add_stock = forms.BooleanField(initial=False, required=False, label="Add Stock")
    reduce_stock = forms.BooleanField(initial=False, required=False, label="Reduce Stock")
    class Meta:
        model = Product
        fields = ["product", "price", "description", "amount"]

# model = Product untuk menunjukkan model yang digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product.
# fields = ["name", "price", "description"] untuk menunjukkan field dari model Product yang digunakan untuk form. Field date_added tidak dimasukkan ke list fields karena tanggal ditambahkan secara otomatis.