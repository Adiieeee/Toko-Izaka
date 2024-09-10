# Tugas 2 PBP
## Link Aplikasi PWS -> [LINKS 🔗](http://muhammad-adiansyah-tokoizakaa.pbp.cs.ui.ac.id/)
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
### Membuat sebuah proyek Django baru.
   1. Buat direktori baru dengan nama `toko-izaka` dan masuk ke dalamnya.
   2. Di dalam direktori tersebut, buka command prompt (Windows)
   3. Buat virtual environment `python -m venv env`
   4. aktifkan virtual environment `env\Scripts\activate`
   5. Di dalam direktori yang sama, buat berkas `requirements.txt` dan tambahkan beberapa dependencies.
      ```
      django
      gunicorn
      whitenoise
      psycopg2-binary
      requests
      urllib3
      ```
   6. Lakukan instalasi terhadap dependencies `pip install -r requirements.txt`
   7. Buat proyek Django bernama `toko_izaka` dengan perintah `django-admin startproject toko_izaka .`
   8. Tambahkan `ALLOWED_HOSTS = ["localhost", "127.0.0.1"]` di `settings.py`
   9. Nonaktifkan virtual environment `deactivate`

### Membuat aplikasi dengan nama `main` pada proyek tersebut.
   1. aktifkan virtual environment `env\Scripts\activate`
   2. membuat aplikasi baru dengan nama `main` dengan perintah `python manage.py startapp main`
   3. Buka berkas `settings.py` di dalam direktori proyek `toko_izaka`, tambahkan `main` ke dalam daftar aplikasi pada variabel `INSTALLED_APPS`
      ```
      INSTALLED_APPS = [
          ...,
          'main'
      ]
      ```

### Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.
   1. Buatlah berkas `urls.py` di dalam direktori `main` lalu isi dengan kode ini
       ```
       from django.urls import path
       from main.views import show_main
      
       app_name = 'main'
      
       urlpatterns = [
           path('', show_main, name='show_main'),
       ]
       ```

### Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut `name`, `price`, `description`.
   1. Buka berkas `models.py` pada direktori aplikasi `main` dan isi dengan
       ```
       from django.db import models

       class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.IntegerField()
          description = models.TextField()
       ```
   2. Jalankan perintah berikut untuk membuat migrasi model `python manage.py makemigrations`
   3. Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal. `python manage.py migrate`

### Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
   1. Buka berkas `views.py` yang terletak di dalam berkas aplikasi `main` lalu tambahkan fungsi `show_main`.
       ```
       from django.shortcuts import render

       def show_main(request):
           context = {
               'toko' : 'Toko Izaka',
               'name' : 'Phantom Mask',
               'image' : 'https://imgur.com/a/U0fYFir',
               'price': '700000',
               'description': 'A mysterious Mask found in the depth of mountains, legend said that this mask once belong the the monkey king itself'
               'nama_kamu' : 'Muhammad Adiansyah',
               'kelas' : 'PBP D'
           }

       return render(request, "main.html", context)
       ```

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
   1. Buka berkas `urls.py` di dalam direktori proyek `toko_izaka`
   2. Impor fungsi `include` dari `django.urls`.
   3. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
       ```
       urlpatterns = [
           ...
           path('', include('main.urls')),
           ...
       ]
       ```

### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
   1. Akses halaman PWS pada https://pbp.cs.ui.ac.id.
   2. Buat proyek baru dengan menekan tombol `Create New Project`
   3. isi `Project Name` dengan `toko-izakaa`. Setelah itu, tekan `Create New Project`
   4. Pada `settings.py` di proyek Django yang sudah kamu buat tadi, tambahkan URL deployment PWS pada `ALLOWED_HOSTS`
   5. Langkah ini perlu kamu lakukan agar proyek Django kamu dapat diakses melalui URL deployment PWS. Lakukan `git add`, `commit`, dan `push` perubahan ini ke repositori GitHub kamu.
   6. Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS, tunggu hingga kelar building lalu bisa pencet tombol `view project`

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
onyongg

## Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
onyongg

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
onyongg

## Mengapa model pada Django disebut sebagai ORM?
oya
