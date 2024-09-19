# Toko Izaka 🎭
### Link Aplikasi PWS -> [LINKS 🔗](https://muhammad-adiansyah-tokoizaka.pbp.cs.ui.ac.id/)
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
- ![{29DFF85E-9753-4B84-BA80-85AE17C46220}](https://github.com/user-attachments/assets/c2b45c25-4b4e-480f-a857-f435e9eecd0d)
- ![{DEE29739-3820-4C95-8538-3187A5DD0C07}](https://github.com/user-attachments/assets/5b1bae5e-f6f9-46b9-bfe1-c766e02f2381)
- ![{8230CE7D-0EC2-4E99-8005-416735E489D5}](https://github.com/user-attachments/assets/44a22d48-2f9a-4671-b7f9-e955c9da3167)
- ![{B71A640F-E8E1-4F3D-A74B-B9A72B13AD58}](https://github.com/user-attachments/assets/03a25d64-35db-41d4-a4c9-a0330dfbac40)



# Tugas 4 PBP
### Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
Dalam Django, `HttpResponseRedirect` dan `redirect` digunakan untuk mengarahkan pengguna ke URL lain. `HttpResponseRedirect` adalah subclass dari `HttpResponse` yang mengarahkan pengguna ke URL tertentu biasanya digunakan dengan URL absolut sehingga lebih manual dan cocok jika kita memerlukan kontrol lebih pada pengolahan URL. redirect adalah fungsi shortcut yang lebih fleksibel dan mudah digunakan, yang dapat menerima berbagai jenis argumen seperti URL absolut atau relatif, nama view, atau objek model. Dengan redirect(), kita dapat melakukan pengalihan dengan lebih cepat dan mudah tanpa harus menulis URL secara manual.

### Jelaskan cara kerja penghubungan model `MoodEntry` dengan `User`!
Setuju

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication dan authorization adalah dua konsep keamanan yang saling berkaitan dalam Django. Authentication adalah proses verifikasi identitas pengguna. Ini memastikan bahwa pengguna adalah siapa yang mereka klaim dengan memeriksa kredensial seperti nama pengguna dan kata sandi. Authorization, di sisi lain, adalah proses menentukan apa yang diizinkan dilakukan oleh pengguna yang telah terautentikasi. Ini mengontrol akses ke sumber daya dan tindakan berdasarkan peran atau izin pengguna.Django mengimplementasikan kedua konsep ini melalui sistem authentication yang terintegrasi. Django menyediakan model User yang menyimpan informasi pengguna dan menangani proses login dan logout. Untuk authentication, Django menggunakan middleware AuthenticationMiddleware yang mengasosiasikan pengguna dengan setiap permintaan menggunakan sesi. Untuk authorization, Django menggunakan sistem izin yang memungkinkan Anda menetapkan izin spesifik ke pengguna atau grup pengguna. Izin ini dapat digunakan untuk mengontrol akses ke view atau tindakan tertentu dalam aplikasi.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan sesi berbasis cookie. Ketika pengguna berhasil login, Django membuat sesi baru dan menyimpan ID sesi dalam cookie di browser pengguna. Setiap kali pengguna mengirimkan permintaan (request) ke server setelah login, browser secara otomatis menyertakan cookie ini. Django kemudian memeriksa ID sesi di cookie untuk mendapatkan informasi tentang pengguna yang login dan mempertahankan status autentikasi mereka selama sesi berlangsung. Kegunaan lain cookies salah satunya adalah Pelacakan preferensi pengguna, Analisis dan pelacakan, Iklan yang dipersonalisasi. Tidak semua cookies aman digunakan, dan keamanan cookie bergantung pada cara pengaturannya. Cookies yang tidak dikonfigurasi dengan benar dapat menimbulkan risiko keamanan. Misalnya, jika cookie berisi informasi sensitif seperti token autentikasi dan tidak diatur sebagai HttpOnly, maka JavaScript yang berbahaya di browser bisa mencurinya melalui serangan XSS (Cross-Site Scripting).

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
   **1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
   - Aktifkan virtual environment terlebih dahulu pada terminal.
   - Buka `views.py` yang ada pada subdirektori `main` pada proyek kamu.
     ```python
     from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
     from django.contrib import messages
     from django.contrib.auth import authenticate, login, logout
     ```
   - Tambahkan fungsi `register`, `login_user`, `logout` di bawah ini ke dalam `views.py`
     ```python
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
     ```
     ```python
     def login_user(request):
        if request.method == 'POST':
           form = AuthenticationForm(data=request.POST)
    
           if form.is_valid():
                 user = form.get_user()
                 login(request, user)
                 return redirect('main:show_main')
    
        else:
           form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
     ```
     ```python
     def logout_user(request):
         logout(request)
         return redirect('main:login')
     ```
   - Buatlah berkas HTML baru dengan nama `register.html` pada direktori `main/template`
     ```python
     {% extends 'base.html' %}

     {% block meta %}
     <title>Register</title>
     {% endblock meta %}
    
     {% block content %}
    
     <div class="login">
       <h1>Register</h1>
    
       <form method="POST">
         {% csrf_token %}
         <table>
           {{ form.as_table }}
           <tr>
             <td></td>
             <td><input type="submit" name="submit" value="Daftar" /></td>
           </tr>
         </table>
       </form>
    
      {% if messages %}
      <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
       </ul>
       {% endif %}
     </div>
    
     {% endblock content %}
     ```

  - Buatlah berkas HTML baru dengan nama `login.html` pada direktori `main/templates`
    ```python
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}
    
    {% block content %}
    <div class="login">
      <h1>Login</h1>
    
      <form method="POST" action="">
        {% csrf_token %}
        <table>
          {{ form.as_table }}
          <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
          </tr>
        </table>
      </form>
    
      {% if messages %}
      <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
      </ul>
      {% endif %} Don't have an account yet?
      <a href="{% url 'main:register' %}">Register Now</a>
    </div>
    
    {% endblock content %}
    ```
  - Bukalah berkas `main.html` yang ada pada direktori `main/templates` dan tambahkan potongan kode di bawah ini
    ```python
    ...
    <a href="{% url 'main:logout' %}">
      <button>Logout</button>
    </a>
    ...
    ```
  - Buka `urls.py` yang ada pada subdirektori `main` dan impor fungsi yang sudah kamu buat tadi.
    ```python
    from main.views import register, login_user, logout_user
    ```
  - Tambahkan path url ke dalam `urlpatterns`
    ```python
        urlpatterns = [
        ...
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ]
    ```
  - 
