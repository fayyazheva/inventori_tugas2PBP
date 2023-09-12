from django.shortcuts import render
def show_main(request):
    context = {
        'product': 'Mochi Daifuku Rasa Strawberry Blueberry',
        'price': 'Rp 150.000',
        'description' : 'Mochi enak, sehat, cocok untuk anak fasilkom karena warnanya merah biru :D',
        'amount' : '100'
    }

    return render(request, "main.html", context)
# Create your views here.

# def show_main(request) merupakan deklarasi fungsi show_main, yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

# context adalah dictionary yang berisi data yang akan dikirimkan ke tampilan. Pada konteks ini, dua data disertakan, yaitu:

# name: Data nama.
# class: Data kelas.
# return render(request, "main.html", context) berguna untuk me-render tampilan main.html dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.
