from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')

def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'kelas' : 'PBP B',
        'app_Name' : 'mochi', 
        'products' : products,
        'last_login': request.COOKIES['last_login'], 
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.image = request.POST.get('image')
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)
    product.image = request.POST.get('image')
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def add_stock(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.amount += 1
    product.save()
    response = HttpResponseRedirect(reverse("main:show_main")) 
    return response

# Tambahkan fungsi untuk mengurangi jumlah stok
@login_required(login_url='/login')
def reduce_stock(request, product_id):
    product = Product.objects.get(pk=product_id)
    response = HttpResponseRedirect(reverse("main:show_main"))
    if (product.amount == 0):
        return response
    product.amount -= 1
    product.save() 
    return response

@login_required(login_url='/login')
def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        product = request.POST.get("product")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user
        image = request.POST.get("image")

        new_product = Product(name=product, price=price, description=description, user=user, amount=amount, image=image)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
# def show_main(request) merupakan deklarasi fungsi show_main, yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
# context adalah dictionary yang berisi data yang akan dikirimkan ke tampilan. Pada konteks ini, dua data disertakan, yaitu:

# name: Data nama.
# class: Data kelas.
# return render(request, "main.html", context) berguna untuk me-render tampilan main.html dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

# form = ProductForm(request.POST or None) digunakan untuk membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.
# form.is_valid() digunakan untuk memvalidasi isi input dari form tersebut.
# form.save() digunakan untuk membuat dan menyimpan data dari form tersebut.
# return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect setelah data form berhasil disimpan.

# Fungsi Product.objects.all() digunakan untuk mengambil seluruh object Product yang tersimpan pada database.
#return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# form = UserCreationForm(request.POST) digunakan untuk membuat UserCreationForm baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.
# form.is_valid() digunakan untuk memvalidasi isi input dari form tersebut.
# form.save() digunakan untuk membuat dan menyimpan data dari form tersebut.
# messages.success(request, 'Your account has been successfully created!') digunakan untuk menampilkan pesan kepada pengguna setelah melakukan suatu aksi.
# return redirect('main:show_main') digunakan untuk melakukan redirect setelah data form berhasil disimpan.

# Singkatnya, function authenticate, login yang diimport diatas akan digunakan untuk melakukan autentikasi dan login jika autentikasi berhasil

# authenticate(request, username=username, password=password digunakan untuk melakukan autentikasi pengguna berdasarkan username dan password yang diterima dari permintaan (request) yang dikirim oleh pengguna saat login

# logout(request) digunakan untuk menghapus sesi pengguna yang saat ini masuk.
# return redirect('main:login') mengarahkan pengguna ke halaman login dalam aplikasi Django.

# login(request, user) berfungsi untuk melakukan login terlebih dahulu
# response = HttpResponseRedirect(reverse("main:show_main")) untuk membuat response
# `response.setcookie('last_login', str(datetime.datetime.now())) berfungsi untuk membuat _cookie last_login dan menambahkannya ke dalam response

# 'last_login': request.COOKIES['last_login'] berfungsi menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web.

# response.delete_cookie('last_login') berfungsi untuk menghapus cookie last_login saat pengguna melakukan logout

# Parameter commit=False yang digunakan pada potongan kode diatas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. Pada kasus ini, kita akan mengisi field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.

# name:  diatas berfungsi untuk menampilkan objek Product yang terasosiasikan dengan pengguna yang sedang login. Hal tersebut dilakukan dengan menyaring seluruh objek dengan hanya mengambil Product yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login.
# Kode request.user.username berfungsi untuk menampilkan username pengguna yang login pada halaman main