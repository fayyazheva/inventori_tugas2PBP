"""
URL configuration for inventori project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]

# Berkas urls.py pada proyek bertanggung jawab untuk mengatur rute URL tingkat proyek.
# Fungsi include digunakan untuk mengimpor rute URL dari aplikasi lain (dalam hal ini, dari aplikasi main) ke dalam berkas urls.py proyek.
# Path URL 'main/' akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main.