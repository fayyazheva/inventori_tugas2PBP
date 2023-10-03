Nama    : Fayya Salwa Azheva
NPM     : 2206826192
Kelas   : PBP B
Link App: https://inventoripbp.adaptable.app/

===========TUGAS 2=================
Penjelasan:
1.  cara mengimplementasikan checklist di atas secara
step-by-step
    a. Membuat sebuah proyek Django
        1. Membuat direktori utama dimana direktori tersebut menjadi repositori lokal. Di dalam direktori utama, kita perlu: 
            a. mengkonfigurasi git 
            b. memnghubungkan repositori lokal dengan repositori github dan membuat branch, di mana saya harus membuat terlebih dahulu repositori yang ada di github
            a. menjalankan virtual virtual environment yang berguna agar aplikasi yang digunakan tidak bertabrakan dengan versi lainnya
            b. membuat berkas requirements.txt
            c. memasang dependencies (pip install -r requirements.txt) dalam keadaan telah menjalankan virtual environment
            d. menambahkankan berkas .gitignore
        2. membuat direktori proyek django. Langkah-langkahnya seperti berikut:
            a. membuat proyek dengan perintah django-admin startproject ((nama proyek)) .
            b. menambahkan * pada ALLOWED_HOST pada settings.py
            c. menjalankan server django. Hal ini memastikan agar manage.py aktif pada shell saat ini. Untuk mengehentikan, gunakan Control+C
        Setelah menjalankan semuanya, maka laukan add, commit, dan push pada github dari direktori repositori lokal (utama)
        3. Deployment Adaptable.io
            a. Pastikan memiliki akun adabtable.io yang terhubung dengan github
            b. login, buat aplikasi baru, dan hubungkan dengan repositori yang sesuai pada github
            c. memilih template deployment yakni python dan basis data yang digunakan yakni PostgreSQL
            d. pilih versi python yang sesuai dan masukkan python manage.py migrate && gunicorn ((nama direktori)).wsgi
            e. pilih nama aplikasi untuk jadi domain web
            f. centang bagian HTTP Listener on PORT dan klik Deploy App
2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html   
![This is an image](/Bagan.png)

3. mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer dan memastikan apabila versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lainnya. 


4. apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
MVC (Model-View-Controller):
    Model: untuk mengelola data aplikasi dan logika, berhubungan dengan database dan pemrosesan data
    View: Menampilkan informasi kepada pengguna dan mengambil input dari mereka, berhubuhngan degan user interface
    Controller: mengendalikan alur aplikasi dan berfungsi sebagai penghubung antara Model dan View. 

    MVC  berfokus pada pemisahan antara Model, View, dan Controller, dengan Controller bertanggung jawab untuk mengendalikan alur aplikasi.

MVT (Model-View-Template):
    Model: untuk mengelola data aplikasi dan logika, berhubungan dengan database dan pemrosesan data
    View: menangani alur aplikasi, memproses permintaan, dan mengatur respons. 
    Template: Menangani tampilan UI dan mengatur cara data dari Model akan ditampilkan kepada pengguna.
  
    Pada MVT, peran View lebih dekat dengan Controller daripada View dalam MVC. View mengatur alur aplikasi dan respons, dan Template menangani tampilan UI.

MVVM (Model-View-ViewModel):
    Model: untuk mengelola data aplikasi dan logika, berhubungan dengan database dan pemrosesan data
    View: Menampilkan data ke pengguna, tetapi tidak memiliki logika. Dalam MVVM, View lebih pasif dan tidak menangani interaksi pengguna secara langsung.
    ViewModel: Menyediakan abstraksi antara Model dan View, mengambil data dari Model dan memformatnya untuk ditampilkan di View. 
    
    MVVM merupakan pola yang umumnya digunakan dalam pengembangan aplikasi berbasis UI, seperti aplikasi seluler atau desktop. Dalam hal ini menekankan pemisahan tugas antara View yang pasif dan ViewModel yang aktif dalam mengelola logika tampilan dan interaksi pengguna.


===========TUGAS 3=================
1. Apa perbedaan antara form POST dan form GET dalam Django?

    form POST digunakan untuk mengirim data dari user ke server untuk diolah dan disimpan dimana pengiriman data tersebut mengubah status atau data di server, seperti menambahkan, mengedit, atau menghapus suatu entitas pada database

    form GET juga digunakna untuk mengirim data dari user ke server, namun pengirim data tidak memengaruhi status atau data di server, seperti pencarian atau pengambilan data dari server

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    XML -> self-descriptive, dapat mengerti informasi apa yang ingin disampaikan dari data tertulis dan dibungkus di dalam tag. contoh:
        <?xml version="1.0" encoding="UTF-8"?>
        <person>
            <name>Fayya Salwa</name>
            <age>19</age>
            <address>
                <street>37 Palakali</street>
                <city>Depok</city>
                <zip>51111</zip>
            </address>
        </person>

    JSON -> self-describing, jauh lebih mudah dimengerti mengenai informasi yang ditulis. Sintaksnya merupakan turunan dari object JavaScript, namun formatnya berbentuk text. Data disimpan dalam bentuk key dan value. contoh:
        {
            "name": "Fayya Salwa",
            "age": 19,
            "address": {
                "street": "37 Palakali",
                "city": "Depok",
                "zip": "51111"
            }
        }
    
    HTML -> tidak berkaitan lengsung dengan pengiriman data, HTML  digunakan untuk membuat tampilan halaman web dan mengatur tampilan konten yang akan ditampilkan. contoh:
        <!DOCTYPE html>
        <html>
        <head>
            <title>Data XML</title>
        </head>
        <body>
            <person>
                <name>Fayya Salwa</name>
                <age>19</age>
                <address>
                    <street>37 Palakali</street>
                    <city>Depok</city>
                    <zip>51111</zip>
                </address>
            </person>
        </body>
        </html>
    maka, HTML hanya digunakan untuk menampilkan struktur data XML atau JSON di peramban web namun tidak melakukan pemrosesan data
  
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    karena JSON didesain self-describing dimana sangat mudah dimengerti oleh user dan sintaksnya merupakan turunan dari object pada JavaScript yang formatnya berupa text. Selain itu Data pada JSON disimpan dalam bentuk key dan value yang berupa tipe data primitif (string, number, boolean) dan berupa objek. 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
     -membuat form sederhana untuk menginput data-data pada aplikasi agar nantinya kita dapat menambahkan data baru yang akan ditampilkan pada halaman utama. dalam hal ini kita 
        - membuat berkas python form tersebut, lalu:
            - menambahkan model yang digunakan form tersebut
            - menentukan objek untuk  menyimpan isi dari form tersebut
            - menentukan field dari model objek tersebut, contohnya nama product, price, description, amount, dsb.

    -menambahkan beberapa pada bagian views.py seperti:
        - import
            from django.http import HttpResponseRedirect
            from main.forms import ProductForm
            from django.urls import reverse
            
             digunakan untuk melakukan redirect halaman web ke URL lain, membuat instance dari form dan menggunakannya dalam tampilan Django Anda untuk mengolah data, dan mengimport fungsi yang membantu dalam menghasilkan URL berdasarkan nama dari pola URL proyek django.

        - fungsi baru yang menerima parameter request dan menghasilkan formulir yang dapat menambahkan data secara otomatis ketika user submit pada sebuah form

    -mengubah fungsi show_main pada view.py agar dapat mengambil seluruh object product yang tersimpan pada database

    -mengimport fungsi baru yang telah ditambahkan di views.py dan menambahkan path urlnya ke urlpatterns yang telah ada sebelumnya

    2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

    [HTML] 
    - membuat berkas HTML baru yang berisi
     - inisiasi block form menggunakan metode POST
     - token sebagai security yang digenerate secara otomatis oleh django
     - sesuatu yang dapat menampilkan fields form pada form python yang telah dibuat
     - tombol submit untuk mengirim request ke view fungsi baru
    - menambahkan kode pada main.html yang telah dibuat sebelumnya yang dapat menampilkan data product dalam bentuk tabel dan tombol yang akan redirect ke halaman form 
    
    [XML/JSON/XML by ID/JSON by ID]
    - membuat fungsi yang menerima paramater request untuk XML, JSON, XML by ID, dan JSON by ID yang berisi 
        - variabel untuk menyimpan hasil query seluruh data
        - return fuction yang berisi data hasil query yang diserialisasi menjadi XML/JSON/XML by ID/JSON by ID
    - import fungsi-fungsi tersebut pada urls.py
    - menambahkan path url pada urlspatterns fungsi-fungsi tersebut

3.  Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    - mengimport fungsi-fungsi yang telah dibuat ke urls.py yang ada folder main:
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

    - menambahkan path url pada urlspatterns fungsi-fungsi tersebut
        [HTML]
        path('create-product', create_product, name='create_product')
        [XML]
        path('xml/', show_xml, name='show_xml')
        [JSON] 
        path('json/', show_json, name='show_json'),
        [XML by ID]
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id')
        [JSON by ID]
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id')

akses XML, JSON, XML by ID, dan JSON by ID pada postman
![This is an image](/POSTMAN_HTML.png)
![This is an image](/POSTMAN_JSON.png)
![This is an image](/POSTMAN_XML.png)
![This is an image](/POSTMAN_XML_ID.png)
![This is an image](/POSTMAN_JSON_ID.png)  



===========TUGAS 4=================

1.  Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

UserCreationForm merupakan impor formulir bawaan dari Django yang memudahkan pembuatan formulir pendaftaran user pada aplikasi web. 

Kelebihan:
    - UserCreationForm sudah termasuk fitur keamanan, seperti hashing password, untuk melindungi data pengguna
    - Form ini mudah diintegrasikan dengan sistem otentikasi Django, sehingga pengguna dapat dengan cepat mendaftar dan masuk ke dalam aplikasi
    - UserCreationForm dapat disesuaikan dengan mudah dengan menambahkan bidang tambahan atau mengubah tampilan sesuai kebutuhan aplikasi

Kekurangan:
    - UserCreationForm hanya mencakup elemen-elemen dasar seperti username, password, dan email. Jika memerlukan bidang tambahan atau fitur-fitur pendaftaran yang lebih kompleks, perlu menyesuaikan form ini atau membuat form khusus sendiri
    - Form ini tidak secara otomatis mengatur atau mengirim email verifikasi saat pengguna mendaftar. Perlu menambahkan langkah-langkah tambahan untuk mengimplementasikan verifikasi email jika diperlukan
    - UserCreationForm memiliki tampilan standar, yang mungkin tidak sesuai dengan desain atau gaya visual tertentu yang diinginkan oleh pengembang atau perancang web

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Autentikasi: memeriksa identitas pengguna dengan memverifikasi data yang dimiliki user, biasanya berupa username dan password. Hal ini digunakan untuk memastikan hanya user tertntu saja yang dapat memiliki akses ke suatu aplikasi web.

    Otorisasi: proses mengendalikan hak ases pengguna terotentikasi pada fitur-fitur tertentu pada aplikasi web. Hal ini digunakan untuk menentukan role pada setiap user agar dapat mengakes ke bagian atau fitur sesuai dengan role nya tersebut

    Kedua hal tersebut penting karena kedua hal tersebut membantu melindungi aplikasi dari akses user yang tidak terdaftar atau tidak terotentikasi serta dapat memastikan bahwa user mendapat akses yang sesuai dengan rolenya. Hal ini meningkatkan keamanan aplikasi web tersebut serta pengembang dapat mengelola peran user dengan baik.


3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    Cookies adalah data yang disimpan pada client side dalam bentuk teks oleh server web saat user mengunjungi situs web tersebut. Cookies dalam konteks aplikasi web dugunakan untuk untuk menyimpan informasi dari perangkat user, yang dapat diakses dan digunakan oleh server web saat user mengakses situs tersebut kembali.

    Django menggunakan cookies untuk mengelola data sesi user dengan mengatur konfigurasi mengeni nama cookie, expire time, dan domain terkait dengan cookie. Selain itu, django menggunakan cookies untuk menyimpan data sesi pengguna seperti ID pengguna, preferesi, dan lain-lain.  


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    Penggunaan cookies aman secara default dalam pengembangan web apabila menerapkan temporary cookie. Hal ini dikarenakan data disimpan dalam memori browser dan apabila browser ditutup, maka data akan terhapus. Selain itu, data yang disimpan oleh browser tidak dapat digunakan untuk melacak informasi jangka panjang dan data hanya dapat diakses oleh browser saja.

    Namun, tentu ada risiko potensial yang harus diwaspadai apabila menggunakan cookies secara default. Beberapa risiko tersebut yakni pencurian data pribadi apabila penggunaan cookie menyimpan informasi sensitif seperti otentikasi, kartu kredit, dan data pribadi lainnya. Hal tesrbut dapat dimanfaatkan oleh pihak yang tidak bertanggung jawab untuk mentracking data  yang melanggar privasi user serta mencuri atau memanipulasi cookies yang dikirimkan antara klien dan server. 
    

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    step yang dijalankan pada implementasi fungsi, login, dan logout sama. Namun, beberapa hal seperti impor, kode pada fungsi, dan lain-lain berbeda.

        A. Registrasi
            - Untuk mengimplementasikan fungsi registrasi, kita memanfaatkan UserCreationForm yang merupakan impor formulir bawaan untuk membuat formulir pendaftaran. impor UserCreationForm ditambahkan pada view.py bersama dengan impor redirec dan messages
            - menambahkan fungsi register pada views.py yang berisi kode untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form
            - membuat tampilan register dengan membuat berkas html baru yang berisi template django yang berisi elemn-elemen form seperti tampilan pesan pada pengguna, dan lain-lain
            - mengimpor fungsi register tersebut ke urls.py untuk menghubungkan url dengan view register
            - menambahkan path url ke urlpatterns agar dapat mengakses fungsi yang telah diimpor
        B. Login
            - mengimpor authenticate dan login untuk melakukan autentikasi dan login jika autentikasi berhasil
            - menambahkan fungsi login yang berisi kode untuk mengautentikasi pengguna yang ingin login. Dalam hal ini, kita melakukan autentikasi pengguna berdasarkan username dan password yang diterima dari permintaan (request) yang dikirim oleh pengguna saat login
            - mambuat berkas HTML untuk login yang berisi template untuk menampilkan halaman login aplikasi web django serta elemen-elemen login seperti judul halaman, formulir login, pesan kesalahan, dan lain-lain
            - mengimpor fungsi login tersebut ke urls.py untuk menghubungkan url dengan view login
            - menambahkan path url login ke urlpatterns agar dapat mengakses fungsi yang telah diimpor
        
        c. Logout
            - mengimpor modul django logout untuk proses keluar atau logout user
            - menambahkan kode pada fungsi logout yang berfungsi untuk melakukan mekanisme logout, seperti menghapus sesi pengguna yang sedang masuk dan mengarahkan pengguna ke halaman login aplikasi
            - menambahkan kode pada main.html yang telah dibuat sebelumnya untuk membuat button logout
            - mengimpor fungsi logout tersebut ke urls.py untuk menghubungkan url dengan view logout
            - menambahkan path url logout ke urlpatterns agar dapat mengakses fungsi yang telah diimpor

    setelah membuat fungsi registrasi, login , dan logout, kita melaukan restriksi halaman main agar dapat mengharuskan user masuk atau login sebelum mengakses  halaman web

        - menambahkan impor login_required pada views.py
            from django.contrib.auth.decorators import login_required
        - menambahkan kode kode agar halaman main hanya dapat diakses oleh pengguna yang sudah login atau terautentikasi 
            ...
            @login_required(login_url='/login')
            def show_main(request):
            ...
    
    Dalam aplikasi ini, kita dapat memanfaatkan cookies untuk menyimpan data login pengguna

    - mengimpor HttpResponseRedirect yang merupakan jenis respons untuk mengarahkan pengguna ke url lain, reverse untuk menghasilkan url berdasarkan nama url yg telah didefinisikan dalam konfigurasi url, dan datetime untuk menggunakan tanggal dan waktu yang akan dimanfaatkan pada data login user

    - pada fungsi login_user akan ditambahkan cookie last_login untuk mengetahui terakhir kali user login.
    ...
    if user is not None:
        login(request, user) //user melakukan login terlebih dahulu
        response = HttpResponseRedirect(reverse("main:show_main"))  //membuat respons login
        response.set_cookie('last_login', str(datetime.datetime.now())) //
        return response
    ...

    - menambahkan kode pada show_main pada variabel context untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    - mengubah fungsi logout_user untuk menghapus cookie last_login saat pengguna melakukan logout
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    
    - menampilkan data last login pada tampilan aplikasi dengan cara menambahkan kode berikut pada main.html 
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...


    2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    
        - jalankan proyek django dengan perintah python manage.py runserver pada terminal
        - buka  http://localhost:8000/

        setiap akun akan menjalankan step berikut: 

        - buat akun dengan menekan tulisan Register Now
        - Masukkan username, password, dan password confirmation, dan klik daftar
        - Login sesuai dengan username dan password akun yang telah dibuat sebelumnya, klik login
        - klik Add New Product dan isi product, price, description, dan amount pada form tersebut lalu klik add product, ulangi selama 3 kali untuk menambahkan 3 product yang berbeda-beda
        - logout untuk memasukkan akun yang lain
    
    
    3.  Menghubungkan model Item dengan User.
        Pengguna dapat melihat produk-produk yang telah dibuatnya yang hanya terorisasi pada produknya masing-masing

        - pada models.py, tambahkan kode
            from django.contrib.auth.models import User
           untuk mengimpor model user untuk mengelola user dalam otentikasi 
        - menambahkan model Product untuk menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user

        class Product(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            ...

        - pada views.py, ubah kode menjadi 

            def create_product(request):
                form = ProductForm(request.POST or None)

                if form.is_valid() and request.method == "POST":
                    product = form.save(commit=False)
                    product.user = request.user
                    product.save()
                    return HttpResponseRedirect(reverse('main:show_main'))
                ...
            dimana parameter commit=False digunakan untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. 

        - mengubah kode pada fungsi show_main 
            def show_main(request):
                products = Product.objects.filter(user=request.user)

                context = {
                    'name': request.user.username,
                ...
            ...

            hal ini berfungsi untuk  menampilkan objek Product yang terasosiasikan dengan pengguna yang sedang login dan  menyaring seluruh objek dengan hanya mengambil Product yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login
        
        karena telah mengubah model, maka kita akan melakukan migrasi model dengan cara 
        python manage.py makemigrations

        lalu pilih no 1 dan ketik kembali angka 1
        lalu jalankan python manage.py migrate

    4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
        
        1. membuka fitur inspect element dengan shortcut ctrl+shift+c
        2. klik bagian Application/Sytorage
        3. klik bagian cookies
        
        Dari situ akan terlihat last login, csrftoken, sessionid

        tentunya untuk melihat data tersebut, user harus login terlebih dahulu. Karena ketika logout, data tersebut akan otomatis hilang

===========TUGAS 5=================
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    a. Element Selector
        memungkinkan pengguna untuk mengubah properti untuk semua elemen yang memiliki tag HTML yang sama.
        Penggunaanya saat kita menggunakan element sebagai selector dalam file CSS. Hal ini juga dapat digunnakan ketika  ingin menerapkan gaya ke semua elemen dengan tag HTML yang sama. Element selector menggunakan format [id_name]
    b. ID Selector
        ID selector menggunakan ID pada tag sebagai selector-nya di mana ID bersifat unik dalam satu halaman web. ID dapat ditambahkan pada halaman template HTML. Dalam hal ini, pengguna dapat menggunakan ID tersebut sebagai selector dalam file CSS. Penggunaanya saat pengguna ingin menerapkan gaya menggaya elemen yang memiliki ID tertentu dan hanya ada satu elemen dengan ID tersebut dalam halaman. ID selector menggunakan format #[id_name] (selalu diawali #)
    c. Class Selector
        Class Selector memungkinkan kita untuk mengelompokkan elemen dengan karakteristik yang sama. Penggunaan Class tersebut sebagai selector dalam file CSS dan digunakan saat  ingin menerapkan gaya yang sama ke beberapa elemen yang memiliki kelas yang sama. Class selector menggunakan format .[class_name] (diawali .)


 2. Jelaskan HTML5 Tag yang kamu ketahui.
 <title>: Digunakan untuk menentukan judul halaman web yang akan ditampilkan di bilah judul browser.

<link>: Umumnya digunakan untuk menghubungkan halaman web dengan berkas CSS eksternal atau untuk mengatur favicon.

<style>: Ini adalah tag untuk menentukan aturan gaya CSS dalam halaman HTML atau secara internal.

<body>: Bagian utama dari halaman web yang berisi konten yang akan ditampilkan kepada pengguna.

<h1>, <h2>, ..., <h6>: Digunakan untuk menandai tingkat judul (dari yang terpenting hingga yang kurang penting) dalam halaman web.

<p>: Untuk membuat paragraf teks.

<a>: Digunakan untuk membuat tautan (hyperlink) ke halaman web lain atau sumber daya.

<img>: Untuk menampilkan gambar dalam halaman web.

<ul>: Digunakan untuk membuat daftar tak berurutan (unordered list).

<ol>: Digunakan untuk membuat daftar terurut (ordered list).

<li>: Digunakan untuk menandai setiap item dalam daftar (<ul> atau <ol>).

<div>: Elemen divisual yang sering digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML lainnya.

<span>: Elemen inlinesering digunakan untuk mengapit atau menerapkan gaya pada teks atau elemen kecil lainnya.


3. Jelaskan perbedaan antara margin dan padding.

Margin
-merupakan jarak antara elemen dengan elemen-elemen di luar elemen tersebut, sehingga mempengaruhi tata letak elemen terhadap elemen lain di sekitarnya.
- tidak memiliki latar belakang (background) dan tidak akan tampil sebagai bagian dari elemen itu sendiri.
- digunakan untuk mengatur jarak antara elemen dengan elemen-elemen luar, seperti elemen lain di sekitarnya atau batas area konten (misalnya, jarak antara dua kotak di dalam tata letak).

Padding:

-merupakan jarak antara konten dalam elemen dengan tepi elemen itu sendiri. Ini mempengaruhi bagian dalam dari elemen, termasuk area konten dan batasnya.
-dapat memiliki latar belakang (background) dan akan tampil sebagai bagian dari elemen, sehingga mengubah warna atau gambar latar belakang di dalam elemen.
-digunakan untuk mengatur jarak antara konten elemen dan tepi elemen tersebut.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Tailwind
-Tailwind CSS membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.	Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.
-Tailwind CSS memiliki file CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada	Bootstrap memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan.
-Tailwind CSS memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek	Bootstrap sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.
-Tailwind CSS memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.

Bootsrtap
-Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.
-Bootstrap memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.
-Bootstrap memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan.
-Bootstrap sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.

Kapan Menggunakan Bootstrap:

Ketika ingin membangun situs web dengan cepat menggunakan komponen-komponen UI yang telah dirancang sebelumnya.
Ketika memiliki batasan waktu dan perlu menyelesaikan proyek dengan cepat.
Ketika tidak memiliki pengalaman dalam menyesuaikan desain dengan CSS.

Kapan Menggunakan Tailwind CSS:

Ketika memerlukan tingkat customisasi yang tinggi dan ingin mendesain tampilan yang sangat khusus.
Ketika ingin mengurangi ukuran file CSS dan memaksimalkan kinerja situs.
Ketika memiliki pengetahuan yang baik tentang CSS atau ingin belajar lebih mendalam tentang CSS.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut

        -Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
        -Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

    Jawaban:
    1. halaman login
    pada halaman login sendiri, kita dapat mencari template html dan css dari sumber tertera atau sumber lainnya. Ketika kita menggunakan template atau framework, kita harus pastikan bahwa data yang digunakan pada login sesuai dengan apa yang telah kita buat sebelumnya, yakni username dan password.

    Selain itu, kita juga menyediakan label register apabila user belum mwemiliki akun. label tersebut nantinya akan di-link ke laman register

    2. Register
    Pada laman register, kita telah mengimplementasikan {{ form.as_table }} yang merupakan sebuah form dalam template django. dalam hal ini, penting bagi kita untuk mengetahui bagaimana untuk men-styling {{ form.as_table }}  karena pemanggilan objectnya akan sedikit berbeda dari form login atau lainnya. 

    3. Ketika 2 halaman ini telah dikustomisasi, pastikan bahwa kita mengklik submit pada register, kita harus kembali ke login, bukan ke halaman main. pastikan semua button berfungsi pada semestinya

    4. Main
    karena kita menggunakan card pada halaman ini, pastikan bahwa isi pada card tersebut merupakan sebuah looping dari produk yang anda ciptakan. Pada hal ini, ketika kita menambah product, otomatis akan menambah card tersebut. Pastikan bahwa keterangan-keterangan pada produk tertulis pada card tersebut dan juga elemen pendukung lainnya seperti button tambah product, nama aplikasi, identitas, button logout, last eddited date tercantum dengan baik

    5. Tambah product dan edit product
    kedua halaman ini memiliki inteface yang sama, sehingga implementasi kodenya juga akan sama. Sama halnya dengan register, halaman ini menggunakan {{ form.as_table }} sehingga perlu sedikit ketelitian untuk men-styling tiap objek halaman tersebut
    
    