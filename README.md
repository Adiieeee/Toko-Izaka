# Toko Izaka 🎭
### Link Aplikasi PWS -> [LINKS 🔗](http://muhammad-adiansyah-tokoizakaa.pbp.cs.ui.ac.id/)
# Tugas 2 PBP
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
   **1. Membuat sebuah proyek Django baru.**
   - Buat direktori baru dengan nama `toko-izaka` dan masuk ke dalamnya.
   - Di dalam direktori tersebut, buka command prompt (Windows)
   - Buat virtual environment `python -m venv env`
   - aktifkan virtual environment `env\Scripts\activate`
   - Di dalam direktori yang sama, buat berkas `requirements.txt` dan tambahkan beberapa dependencies.
      ```python
      django
      gunicorn
      whitenoise
      psycopg2-binary
      requests
      urllib3
      ```
   - Lakukan instalasi terhadap dependencies `pip install -r requirements.txt`
   - Buat proyek Django bernama `toko_izaka` dengan perintah `django-admin startproject toko_izaka .`
   - Tambahkan `ALLOWED_HOSTS = ["localhost", "127.0.0.1"]` di `settings.py`
   - Nonaktifkan virtual environment `deactivate`

   **2. Membuat aplikasi dengan nama `main` pada proyek tersebut.**
   - Aktifkan virtual environment `env\Scripts\activate`
   - Membuat aplikasi baru dengan nama `main` dengan perintah `python manage.py startapp main`
   - Buka berkas `settings.py` di dalam direktori proyek `toko_izaka`, tambahkan `main` ke dalam daftar aplikasi pada variabel `INSTALLED_APPS`
      ```python
      INSTALLED_APPS = [
          ...,
          'main'
      ]
      ```

   **3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.**
   - Buatlah berkas `urls.py` di dalam direktori `main` lalu isi dengan kode ini
       ```python
       from django.urls import path
       from main.views import show_main
      
       app_name = 'main'
      
       urlpatterns = [
           path('', show_main, name='show_main'),
       ]
       ```

   **4. Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut `name`, `price`, `description`.**
   - Buka berkas `models.py` pada direktori aplikasi `main` dan isi dengan
       ```python
       from django.db import models

       class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.IntegerField()
          description = models.TextField()
       ```
   - Jalankan perintah berikut untuk membuat migrasi model `python manage.py makemigrations`
   - Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal. `python manage.py migrate`

   **5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
   - Buka berkas `views.py` yang terletak di dalam berkas aplikasi `main` lalu tambahkan fungsi `show_main`.
       ```python
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

   **6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**
   - Buka berkas `urls.py` di dalam direktori proyek `toko_izaka`
   - Impor fungsi `include` dari `django.urls`.
   - Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
       ```python
       urlpatterns = [
           ...
           path('', include('main.urls')),
           ...
       ]
       ```

   **7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
   - Akses halaman PWS pada https://pbp.cs.ui.ac.id.
   - Buat proyek baru dengan menekan tombol `Create New Project`
   - isi `Project Name` dengan `toko-izakaa`. Setelah itu, tekan `Create New Project`
   - Pada `settings.py` di proyek Django yang sudah kamu buat tadi, tambahkan URL deployment PWS pada `ALLOWED_HOSTS`
   - Langkah ini perlu kamu lakukan agar proyek Django kamu dapat diakses melalui URL deployment PWS. Lakukan `git add`, `commit`, dan `push` perubahan ini ke repositori GitHub kamu.
   - Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS, tunggu hingga kelar building lalu bisa pencet tombol `view project`

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![image](https://github.com/user-attachments/assets/fb42c6fe-42ee-45d4-9173-2f0df1400b2e)

### Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
#### Git adalah sebuah sistem kontrol versi (version control system) yang sangat berguna dalam pengembangan perangkat lunak. Git mempunyai banyak seperti:
1. **Sistem kontrol versi**\
   Git dapat melacak perubahan yang dilakukan pada kode. Dengan begitu, kita bisa melihat sejarah perubahan suatu file atau proyek secara lengkap.
2. **Kolaborasi**\
   Git memungkinkan beberapa pengembang bekerja secara simultan pada proyek yang sama. Setiap pengembang memiliki salinan proyek (repository) sendiri, sehingga bisa bekerja secara independen
3. **Reverty atau kembali ke versi sebelumnya**\
   Jika terjadi kesalahan atau bug dalam kode, Git memudahkan pengembang untuk kembali ke versi sebelumnya dari proyek tersebut.
4. **Backup**\
   Git secara otomatis membuat backup dari kode Anda. Jika terjadi masalah pada komputer atau data hilang, Anda bisa memulihkan kode dari backup Git.
5. **Cabang (Branching)**\
   Git mendukung pembuatan cabang (branch) yang memungkinkan pengembang untuk bekerja pada fitur baru secara terpisah tanpa mengganggu kode utama. Cabang ini bisa digabungkan kembali ke kode utama ketika fitur tersebut sudah selesai.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django mudah dipelajari, Django dirancang untuk memudahkan pengembang dalam membuat aplikasi web dengan cepat dan efisien dan Django memiliki dokumentasi yang sangat baik dan menyeluruh. Hal ini membuat pemula lebih mudah memahami konsep-konsep dasar dalam pengembangan web, seperti routing, views, models, dan templates.

### Mengapa model pada Django disebut sebagai ORM?
ORM adalah singkatan dari Object-Relational Mapper. ORM adalah teknik yang digunakan untuk memetakan objek dalam bahasa pemrograman dengan tabel dan kolom dalam database relasional. Dalam Django, ORM digunakan untuk mengelola interaksi antara model Python dengan database. Model Python adalah kelas yang merepresentasikan struktur data dalam aplikasi. Setiap atribut dalam model Python dipetakan ke kolom dalam tabel database.



# Tugas 3 PBP
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dalam pengimplementasian sebuah platform sangat penting karena memungkinkan platform tersebut berfungsi secara optimal dan efisien dalam mengirimkan, menerima, dan mengelola data yang dibutuhkan untuk operasionalnya. Dalam konteks platform, data delivery berperan sebagai "pembuluh darah" yang mengaliri informasi dari berbagai sumber ke berbagai tujuan. Tanpa data delivery yang efektif, sebuah platform tidak akan berfungsi dengan baik.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Secara umum JSON lebih populer karena XML karena:
1. **Kesederhanaannya dalam membaca**\
  JSON memiliki sintaks yang lebih sederhana dan lebih mudah dibaca serta ditulis dibandingkan XML. JSON menggunakan pasangan kunci-nilai yang lebih intuitif,       terutama bagi pengembang yang sudah familiar dengan JavaScript
2. **Ukuran file yang lebih kecil**\
  JSON cenderung menghasilkan ukuran file yang lebih kecil dibandingkan XML karena tidak menggunakan tag penutup yang panjang, membuatnya lebih efisien dalam penyimpanan dan transmisi data
3. **Kompatibilitas dengan JavaScript**\
   SON adalah format asli untuk JavaScript, sehingga sangat kompatibel dengan aplikasi web modern yang menggunakan JavaScript. Ini membuat integrasi dan penggunaan JSON lebih mudah dalam pengembangan web
4. **Dukungan untuk Array**\
   JSON mendukung array secara langsung, yang sangat berguna untuk menyimpan dan mengelola kumpulan data. XML, di sisi lain, memerlukan struktur yang lebih kompleks untuk mencapai hal yang sama

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memvalidasi data yang dikirimkan melalui form sebelum data tersebut diproses lebih lanjut, seperti disimpan ke dalam database atau digunakan di dalam aplikasi. Method ini sangat penting dalam proses pengelolaan form, terutama untuk memastikan bahwa data yang diterima adalah valid dan sesuai dengan aturan atau batasan yang telah ditentukan.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dalam Django diperlukan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yang merupakan salah satu bentuk serangan keamanan di mana penyerang mencoba mengeksploitasi sesi pengguna yang telah terautentikasi untuk mengirimkan permintaan berbahaya ke server tanpa sepengetahuan atau persetujuan pengguna.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.**
   - Buat direktori templates pada direktori utama (root folder) dan buatlah sebuah berkas HTML baru bernama base.html.
     ```python
     {% load static %}
     <!DOCTYPE html>
     <html lang="en">
       <head>
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         {% block meta %} {% endblock meta %}
       </head>
    
       <body>
         {% block content %} {% endblock content %}
       </body>
     </html>
     ```
   - Buka `settings.py` yang ada pada direktori proyek toko_izaka dan tambahkan kode dibawah
     ```python
     ...
     TEMPLATES = [
         {
             'BACKEND': 'django.template.backends.django.DjangoTemplates',
             'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
             'APP_DIRS': True,
             ...
         }
     ]
     ...
     ```
   - Buat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data Product baru
     ```python
     from django.forms import ModelForm
     from main.models import Product
    
     class ProductForm(ModelForm):
         class Meta:
             model = Product
             fields = ["name", "price", "description", "image"]
     ```
   - Buka berkas `views.py` yang ada pada direktori `main` dan tambahkan
     ```python
     from django.shortcuts import render, redirect
     from main.forms import ProductForm
     from main.models import Product
     ```
   - Buat fungsi baru dengan nama `create_product` yang menerima parameter `request`
     ```python
     def create_product(request):
     form = ProductForm(request.POST or None)

     if form.is_valid() and request.method == "POST":
         form.save()
         return redirect('main:show_main')

     context = {'form': form}
     return render(request, "create_product.html", context)
     ```
   - Ubahlah fungsi `show_mai`n yang sudah ada pada berkas `views.py`
     ```python
     def show_main(request):
     product_entries = Product.objects.all()

     context = {
         'product_entries': product_entries,
     }

     return render(request, "main.html", context)
     ```
   - Buka `urls.py` yang ada pada direktori main dan import fungsi `create_product`
     ```python
     from main.views import show_main, create_product'
     ```
   - Tambahkan path URL ke dalam variabel `urlpatterns` pada `urls.py` di `main`
     ```python
     urlpatterns = [
        ...
        path('create-product', create_product, name='create_product'),
     ]
     ```
   - Buat berkas HTML baru dengan nama `create_product.html` pada direktori `main/templates`
     ```python
     {% extends 'base.html' %} 
     {% block content %}
     <h1>Add New Mood Entry</h1>
    
     <form method="POST">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td>
             <input type="submit" value="Add Mood Product" />
           </td>
         </tr>
       </table>
     </form>
    
     {% endblock %}
     ```
   - Buka `main.html` dan tambahkan kode berikut di dalam `{% block content %}`
     ```python
     {% if not product_entries %}
         <p>Belum ada data product</p>
         {% else %}
         <table>
         <tr>
             <th>name</th>
             <th>price</th>
             <th>description</th>
             <th>image</th>
         </tr>

         {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
         {% endcomment %} 
         {% for product_entry in product_entries %}
         <tr>
             <td>{{product_entry.name}}</td>
             <td>{{product_entry.price}}</td>
             <td>{{product_entry.description}}</td>
             <td><img src="{{ product_entry.image.url }}" alt="Product Image" width="100"></td>
         </tr>
         {% endfor %}
         </table>
         {% endif %}

         <br />

         <a href="{% url 'main:create_product' %}">
         <button>Add New Product</button>
         </a>
     ```
     
   **2. Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
   - Buka `views.py` yang ada pada direktori `main` dan tambahkan import
     ```python
     from django.http import HttpResponse
     from django.core import serializers
     ```
   - Buatlah sebuah fungsi baru yang menerima parameter request dengan nama `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` dan tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
     ```python
     def show_xml(request):
     data = Product.objects.all()
     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```
     ```python
     def show_json(request):
     data = Product.objects.all()
     return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
     ```python
     def show_xml_by_id(request, id):
     data = Product.objects.filter(pk=id)
     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```
     ```python
     def show_json_by_id(request, id):
     data = Product.objects.filter(pk=id)
     return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```

   **3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
   - Buka `urls.py` yang ada pada direktori `main` dan import fungsi tadi
     ```python
     from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
     ```
   - Tambahkan path URL ke dalam `urlpatterns`
     ```python
     ...
     path('xml/', show_xml, name='show_xml'),
     path('json/', show_json, name='show_json'),
     path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
     path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
     ...
     ```

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
Setuju
