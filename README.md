Nama    : Fayya Salwa Azheva
NPM     : 2206826192
Kelas   : PBP B
Link App: https://inventoripbp.adaptable.app/
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




       