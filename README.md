# Toko Izaka 🎭
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
### Git adalah sebuah sistem kontrol versi (version control system) yang sangat berguna dalam pengembangan perangkat lunak. Git mempunyai banyak seperti:
1. **Sistem kontrl versi**
   Git dapat melacak perubahan yang dilakukan pada kode. Dengan begitu, kita bisa melihat sejarah perubahan suatu file atau proyek secara lengkap.
2. **Kolaborasi**
   Git memungkinkan beberapa pengembang bekerja secara simultan pada proyek yang sama. Setiap pengembang memiliki salinan proyek (repository) sendiri, sehingga bisa bekerja secara independen
3. **Reverty atau kembali ke versi sebelumnya**
   Jika terjadi kesalahan atau bug dalam kode, Git memudahkan pengembang untuk kembali ke versi sebelumnya dari proyek tersebut.
4. **Backup**
   Git secara otomatis membuat backup dari kode Anda. Jika terjadi masalah pada komputer atau data hilang, Anda bisa memulihkan kode dari backup Git.
5. **Cabang (Branching)**
   Git mendukung pembuatan cabang (branch) yang memungkinkan pengembang untuk bekerja pada fitur baru secara terpisah tanpa mengganggu kode utama. Cabang ini bisa digabungkan kembali ke kode utama ketika fitur tersebut sudah selesai.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django mudah dipelajari, Django dirancang untuk memudahkan pengembang dalam membuat aplikasi web dengan cepat dan efisien dan Django memiliki dokumentasi yang sangat baik dan menyeluruh. Hal ini membuat pemula lebih mudah memahami konsep-konsep dasar dalam pengembangan web, seperti routing, views, models, dan templates.

## Mengapa model pada Django disebut sebagai ORM?
ORM adalah singkatan dari Object-Relational Mapper. ORM adalah teknik yang digunakan untuk memetakan objek dalam bahasa pemrograman dengan tabel dan kolom dalam database relasional. Dalam Django, ORM digunakan untuk mengelola interaksi antara model Python dengan database. Model Python adalah kelas yang merepresentasikan struktur data dalam aplikasi. Setiap atribut dalam model Python dipetakan ke kolom dalam tabel database.
