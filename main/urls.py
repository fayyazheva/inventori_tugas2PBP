from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_stock, reduce_stock, delete, edit_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-stock/<int:product_id>/', add_stock, name='add_stock'),
    path('reduce-stock/<int:product_id>/', reduce_stock, name='reduce_stock'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
]

# Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.
# Impor path dari django.urls untuk mendefinisikan pola URL.
# Gunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
# Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.