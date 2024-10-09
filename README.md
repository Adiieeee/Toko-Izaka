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
model `MoodEntry` dapat dihubungkan dengan `User` dengan menggunakan **ForeignKey**. dengan ini maka setiap 'MoodEntry' akan terhubung dengan tepat satu pengguna yang sedang login dan hanya akan terhubung ke user yang sesuai.
```python
from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField(max_length=200, null=True, blank=True)
```

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
    
  **2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**
  - saat di login screen pencet Register
  - isi username dan password sesuai kriteria dan setelah submit akun akan terbuat
  - lakukan langkah diatas sebanyak 2x
  - masukan tiga dummy data dengan memencet tombol tambahkan product
  - masukan nama, price, description, dan imagenya lalu tambahkan product
  - lakukan langkah diatas sebanyak 3x
  Meski sudah membuat 3 akun tapi karena kita belum menghubungkan product dengan user maka semua user mempunyai product yang sama.

  **3. Menghubungkan model Product dengan User.**
  - Buka `models.py` yang ada pada subdirektori `main` dan tambahkan kode berikut:
    ```python
    ...
    from django.contrib.auth.models import User
    ...
    ```
  - Pada model `Product` yang sudah dibuat, tambahkan potongan kode berikut:
    ```python
    class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
    ```
  - Buka kembali `views.py` yang ada pada subdirektori `main`, dan ubah potongan kode pada fungsi `create_product`
    ```python
    def create_product(request):
      form = ProductForm(request.POST or None)
  
      if form.is_valid() and request.method == "POST":
          product_entry = form.save(commit=False)
          product_entry.user = request.user
          product_entry.save()
          return redirect('main:show_main')
  
      context = {'form': form}
      return render(request, "create_product.html", context)
    ```
  - Ubah value dari `product_entries` dan `context` pada fungsi `show_main`
    ```python
    def show_main(request):
      product_entries = Product.objects.filter(user=request.user)
    
      context = {
        'name': request.user.username,
    ...
      ```
  - Simpan semua perubahan, dan lakukan migrasi model dengan python `manage.py makemigrations`
  - Pilih `1` untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada database.
    ![{68FC8371-520F-40F3-9768-CE2ECE7F69CE}](https://github.com/user-attachments/assets/61a349d3-6927-422c-b940-bc972d30079f)
  - Ketik angka 1 lagi untuk menetapkan user dengan ID 1
    ![{9BD578F5-6D72-469E-91A5-B83C02ABBCE8}](https://github.com/user-attachments/assets/8bed1803-acae-4404-94cd-6df05a1a6fa1)
  - Lakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.
  - tambahkan sebuah import baru pada `settings.py` yang ada pada subdirektori `toko_izaka`
    ```python
    import os
    ```
  - Kemudian, ganti variabel `DEBUG` dari berkas `settings.py`
    ```python
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
    ```
    
  **4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**
  - Buka kembali `views.py` yang ada pada subdirektori `main`
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
  - Pada fungsi `login_user`, kita akan menambahkan fungsionalitas menambahkan cookie yang bernama `last_login`
    ```python
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
  - Pada fungsi `show_main`, tambahkan potongan kode:
    ```python
    context = {
        'name': request.user.username,
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
    }
    ```
  - Ubah fungsi `logout_user` menjadi seperti potongan kode berikut.
    ```python
    def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
    ```
  - Buka berkas `main.html` dan tambahkan potongan kode berikut
    ```python
    ...
    <h4>User : {{ user.username }}</h4>
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```



# Tugas 5 PBP
### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
- Inline styles: Memiliki prioritas tertinggi, misalnya `<div style="color: red;">`.
- ID selectors: Memiliki prioritas lebih tinggi daripada class dan tag, misalnya `#myId`.
- Class selectors: Memiliki prioritas lebih tinggi daripada tag, misalnya `.myClass`.
- Element Selectors: Prioritas Rendah, paling umum, tetapi juga paling tidak spesifik, misalnya `<p>Ini adalah paragraf</p>`.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Karena responsive design adalah pengembangan web yang membuat situs web dapat menyesuaikan tampilannya secara otomatis sesuai dengan ukuran layar perangkat yang digunakan. Ini berarti, baik pengguna mengakses situs web melalui desktop, laptop, tablet, atau smartphone, mereka akan tetap mendapatkan pengalaman pengguna yang optimal dan konsisten.
**Contoh Aplikasi yang sudah menerapkan responsive design :**
- **Amazon** : Website ini dapat beradaptasi dengan berbagai ukuran layar, menawarkan pengalaman berbelanja yang mulus di perangkat seluler dan desktop.
- **Google** : Baik Google Search maupun Gmail memiliki tampilan yang sangat responsif, sehingga dapat diakses dengan nyaman di berbagai perangkat.
  
**Contoh Aplikasi yang belum menerapkan responsive design :**
- **BBC News** : pada beberapa halaman tertentu yang lebih tua mungkin memiliki tata letak tetap dan tidak menyesuaikan ukuran layar perangkat dengan baik.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**- Margin**
Ruang di luar elemen. Mengatur jarak antara elemen dengan elemen lainnya. Contoh :
```css
.container {
  margin: 20px;
}
```
**- Border**
garis yang mengelilingi padding dan konten elemen. Border dapat memiliki warna, ketebalan, dan gaya. Contoh :
```css
.container {
  border: 2px solid black;
}
```
**- Padding**
```css
.container {
  padding: 10px;
}
```

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**- Konsep Flex Box**

Flexbox adalah model layout yang memungkinkan distribusi ruang dan penataan elemen dalam satu dimensi (baris atau kolom). Elemen yang menggunakan flexbox dapat menyesuaikan ukuran dan posisi secara otomatis berdasarkan ruang yang tersedia, membuatnya sangat berguna untuk tata letak responsif.
Kegunaan: Pengaturan Elemen dalam Baris atau Kolom, Distribusi Ruang, Responsif

**- Konsep Grid Layout**

Grid Layout adalah model layout dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom. Grid memberikan kontrol lebih besar terhadap tata letak, termasuk ukuran dan posisi elemen di berbagai ukuran layar.
Kegunaan: Tata Letak Kompleks, Kontrol yang Lebih Baik, Responsif

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
**1. Implementasikan fungsi untuk menghapus dan mengedit product.**
- Buka `views.py` yang ada pada subdirektori `main` dan buat fungsi baru bernama `edit_product` dan `delete_product`
  ```python
  def edit_product(request, id):
    # Get mood entry berdasarkan id
    product_entries = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product_entries)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
  ```
  ```python
  def delete_product(request, id):
    # Get mood berdasarkan id
    produk_entries = Product.objects.get(pk = id)
    # Hapus mood
    produk_entries.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
  ```
- Tambahkan import pada file `views.py`
  ```python
  from django.shortcuts import .., reverse
  from django.http import .., HttpResponseRedirect
  from main.views import delete_mood
  ```
- Buatlah berkas HTML baru dengan nama `edit_product.html` pada subdirektori `main/templates`
  ```html
  {% extends 'base.html' %}
  {% load static %}
  {% block meta %}
  <title>Edit Product</title>
  {% endblock meta %}
  
  {% block content %}
  {% include 'navbar.html' %}
  <div class="flex flex-col min-h-screen bg-gray-100">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
      <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product</h1>
    
      <div class="bg-white rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6" enctype="multipart/form-data>
            {% csrf_token %}
            {% for field in form %}
                <div class="flex flex-col">
                    <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                        {{ field.label }}
                    </label>
                    <div class="w-full">
                        {{ field }}
                    </div>
                    {% if field.help_text %}
                        <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                    {% endif %}
                    {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
                <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                    Edit Product
                </button>
            </div>
        </form>
    </div>
    </div>
  </div>
  {% endblock %}
  ```
- Buka `urls.py` yang berada pada direktori `main` dan import fungsi tadi
  ```python
  from main.views import edit_product, delete_product
  ```
- Tambahkan path url ke dalam `urlpatterns`
  ```python
  path('edit-product/<uuid:id>', edit_product, name='edit_product'),
  path('delete/<uuid:id>', delete_product, name='delete_product'),
  ```
- Buka `product_details.html` yang berada pada subdirektori `main/templates` (sekarang belum ada tapi nanti akan dibuat). Tambahkan potongan kode berikut
  ```html
  <div class="flex justify-between mt-2">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="flex items-center justify-center w-10 h-10 bg-yellow-500 hover:bg-yellow-600 rounded-full shadow-md transition duration-300">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white" viewBox="0 0 20 20" fill="currentColor">
              <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="flex items-center justify-center w-10 h-10 bg-red-500 hover:bg-red-600 rounded-full shadow-md transition duration-300">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
      </a>
  </div>
  ```
**2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:**
- Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
  **login**
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Login</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
  <style>
  h2 {
      font-family: 'Poppins', sans-serif;
  }
  h3 {
    font-family: 'Poppins', sans-serif;
  }
  </style>
  {% endblock meta %}
  
  {% block content %}
  <div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-black text-4xl font-extrabold text-gray-900">
          Login
        </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <h3>Username<h3>
            <label for="username" class="sr-only">Enter Username</label>
            <input id="username" name="username" type="text" required class="rounded-md appearance-none rounded-none relative block w-full px-3 py-2  border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
          </div>
        </div>
        <div>
          <div>
            <h3>Password<h3>
            <label for="password" class="sr-only">Enter Password</label>
            <input id="password" name="password" type="password" required class="rounded-md appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
          </div>
        </div>
  
        <div>
          <button type="submit" class="rounded-md group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Sign in
          </button>
        </div>
      </form>
  
      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
              <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% elif message.tags == "error" %}
              <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% else %}
              <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% endif %}
        {% endfor %}
      </div>
      {% endif %}
  
      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Don't have an account yet?
          <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```
  **register**
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Register</title>
  {% endblock meta %}
  
  {% block content %}
  <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
          Create your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          {% for field in form %}
            <div class="{% if not forloop.first %}mt-4{% endif %}">
              <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                {{ field.label }}
              </label>
              <div class="relative">
                {{ field }}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  {% if field.errors %}
                    <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                  {% endif %}
                </div>
              </div>
              {% if field.errors %}
                {% for error in field.errors %}
                  <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
              {% endif %}
            </div>
          {% endfor %}
        </div>
  
        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Register
          </button>
        </div>
      </form>
  
      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
      </div>
      {% endif %}
  
      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Already have an account?
          <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Login here
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```
  **create produk**
  ```html
  {% extends 'base.html' %}
  {% load static %}
  {% block meta %}
  <title>Create Product</title>
  {% endblock meta %}
  
  {% block content %}
  
  <div class="flex flex-col min-h-screen bg-gray-100">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
      <h1 class="text-3xl font-bold text-center mb-8 text-black">Create Create Product</h1>
    
      <div class="bg-white shadow-md rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6" enctype="multipart/form-data">
          {% csrf_token %}
          {% for field in form %}
            <div class="flex flex-col">
              <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                {{ field.label }}
              </label>
              <div class="w-full">
                {{ field }}
              </div>
              {% if field.help_text %}
                <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
              {% endif %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
            <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
              Create Product
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  
  {% endblock %}
  ```
- Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
  - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
    ```html
    {% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
      <img src="{% static 'image/orang-binggung.png' %}" alt="Sad face" class="w-64 h-64 mb-4"/>
      <p class="text-center text-gray-600 mt-4">Belum ada data produk</p>
    </div>
    ```
  - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!)
    ```html
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
      {% for product_entry in product_entries %}
      {% include 'product_detail.html' with product_entry=product_entry %}
      {% endfor %}
    </div>
    {% endif %}
    ```
    **kode untuk cardnya**
    ```html
    <div class="relative break-inside-avoid border rounded-lg shadow-md bg-white p-4 mb-6 transition-transform duration-300 hover:shadow-lg">
    <div class="flex flex-col items-left">
        <h3 class="text-2xl font-bold text-gray-800 mb-4 text-center">{{ product_entry.name }}</h3>
        <img src="{{ product_entry.image.url }}" alt="Product Image" class="w-full h-48 object-cover rounded-md mb-4 border border-gray-300">
        <p class="text-lg text-gray-700 mb-2 text-left">Description:</p>
        <p class="text-gray-600 mb-2 text-left">{{ product_entry.description }}</p>
        <p class="text-xl font-bold text-black mb-2">Price: {{ product_entry.price }}</p>
    </div>
    <div class="flex justify-between mt-2">
        <a href="{% url 'main:edit_product' product_entry.pk %}" class="flex items-center justify-center w-10 h-10 bg-yellow-500 hover:bg-yellow-600 rounded-full shadow-md transition duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
        </a>
        <a href="{% url 'main:delete_product' product_entry.pk %}" class="flex items-center justify-center w-10 h-10 bg-red-500 hover:bg-red-600 rounded-full shadow-md transition duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
        </a>
    </div>
    </div>
    ```
- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
  ```html
  <div class="flex justify-between mt-2">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="flex items-center justify-center w-10 h-10 bg-yellow-500 hover:bg-yellow-600 rounded-full shadow-md transition duration-300">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white" viewBox="0 0 20 20" fill="currentColor">
              <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="flex items-center justify-center w-10 h-10 bg-red-500 hover:bg-red-600 rounded-full shadow-md transition duration-300">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
      </a>
  </div>
  ```
- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
  ```html
  <nav class="bg-white shadow-lg fixed top-0 left-0 z-40 w-full">
    <div class="mx-auto flex items-center justify-between p-4">
      <!-- Logo Section -->
      <div class="flex items-center space-x-3">
        <span class="text-2xl font-bold text-black">Toko Izaka</span>
      </div>
  
      <div class="hidden md:flex md:items-center justify-center space-x-8">
        <ul class="flex flex-row space-x-8">
          <li><a href="#" class="text-gray-700 hover:text-indigo-600">Home</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600">About</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600">Services</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600">Pricing</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600">Contact</a></li>
        </ul>
      </div>
  
      <div class="hidden md:flex md:items-center space-x-4">
        {% if user.is_authenticated %}
          <span class="text-gray-700">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded-full transition-all duration-300">Logout</a>
        {% else %}
          <a href="{% url 'main:login' %}" class="bg-indigo-500 hover:bg-indigo-600 text-white font-semibold py-2 px-4 rounded-full transition-all duration-300">Login</a>
          <a href="{% url 'main:register' %}" class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-full transition-all duration-300">Register</a>
        {% endif %}
      </div>
    </div>
    <div class="mobile-menu hidden px-4 w-full md:hidden">
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
  
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
  ```

  

# Tugas 6
### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- **Interaktivitas yang tinggi**
  - **Responsif terhadap pengguna**
    JavaScript memungkinkan elemen-elemen dalam halaman web merespons aksi pengguna secara real-time, seperti ketika pengguna mengklik tombol, mengarahkan kursor, atau mengisi formulir.
  - **Pengalaman pengguna yang lebih baik**
    
    Dengan interaktivitas yang tinggi, pengguna merasa lebih terlibat dan terhubung dengan aplikasi web.
- **Pengolahan data secara real-time**
  
  Dengan JavaScript, aplikasi dapat menangani data pengguna secara langsung, seperti validasi formulir atau menampilkan hasil secara langsung.
- **Kompabilitas lintas platform**
  
  JavaScript dapat dijalankan di berbagai peramban dan platform, memudahkan pengembang untuk membuat aplikasi web yang konsisten.
- **Pemrograman Asinkron**
  
  Dengan AJAX dan Fetch API, memungkinkan aplikasi untuk berkomunikasi dengan server tanpa perlu memuat ulang halaman.


### Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?
Fungsi penggunaan await saat menggunakan fetch() adalah untuk menunggu sampai permintaan HTTP selesai dan menerima responsnya sebelum melanjutkan eksekusi kode. fetch() adalah operasi asinkron, dan await memastikan bahwa hasil dari fetch() dapat diproses setelah respons diterima.
Jika tidak menggunakan await, JavaScript akan melanjutkan eksekusi kode berikutnya tanpa menunggu hasil fetch(), yang bisa menyebabkan kesalahan karena data mungkin belum tersedia saat kode mencoba menggunakannya. Ini dapat menghasilkan nilai Promise yang belum terselesaikan.


### Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?
`csrf_exempt` digunakan untuk menghindari pemeriksaan Cross-Site Request Forgery (CSRF) pada view tertentu. Tanpa decorator ini, permintaan AJAX POST dari halaman web yang sama akan ditolak jika tidak memiliki token CSRF yang valid. Ini adalah langkah keamanan untuk melindungi dari serangan CSRF


### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Karena secara frontend hanya berpengaruh kepada tampilan dan uinya saja tetapi data di databasenya masih ada, oleh karena itu perlu dibersihkan di backend juga untuk memastikan datanya beneran tidak ada

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
**1. Ubahlah kode cards data mood agar dapat mendukung AJAX GET.**
- Bukalah berkas `views.py` dan **hapus dua baris** berikut.
  ```python
   mood_entries = MoodEntry.objects.filter(user=request.user)
  'mood_entries': mood_entries,
  ```
- Bukalah berkas `views.py` dan ubahlah baris pertama views untuk `show_json` dan `show_xml`
   ```python
   data = MoodEntry.objects.filter(user=request.user)
   ```
- Bukalah berkas `main.html.` Hapus bagian block conditional `product_entries`
- tambahkan potongan kode ini di tempat yang sama.
  ```html
  <div id="product_entry_cards"></div>
  ```
- Buatlah block `<script>` di bagian bawah berkas kamu (sebelum `{% endblock content %}`)
   ```html
    async function getProductEntries(){
       return fetch("{% url 'main:show_json' %}").then((res) => res.json())
     }
      ```
- Buatlah **fungsi baru** pada block `<script>` dengan nama `refreshProductEntries`
  ```html
     async function refreshProductEntries() {
     document.getElementById("product_entry_cards").innerHTML = "";
     document.getElementById("product_entry_cards").className = "";
     const productEntries = await getProductEntries();
     let htmlString = "";
     let classNameString = "";

     if (productEntries.length === 0) {
         classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
         htmlString = `
           <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
             <img
               src="{% static 'image/orang-binggung.png' %}"
               alt="Sad face"
               class="w-64 h-64 mb-4"
             />
             <p class="text-center text-gray-600 mt-4">Belum ada data produk</p>
           </div>
        ` ;
     }
     else {
         classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
         productEntries.forEach((item) => {
             htmlString += `
             <div
               class="relative border break-inside-avoid rounded-lg shadow-md bg-white p-4 mb-6 transition-transform duration-300 hover:shadow-lg"
             >
               <div class="flex flex-col items-left">
                 <h3 class="text-2xl font-bold text-gray-800 mb-4 text-center">
                   ${item.fields.name}
                 </h3>
                 <img
                   src="media/${item.fields.image}"
                   alt="Product Image"
                   class="w-54 h-54 mx-auto object-cover rounded-md mb-4 border border-gray-300"
                 />
                 <p class="text-lg text-gray-700 mb-2 text-left">Description:</p>
                 <p class="text-gray-600 mb-2 text-left">${item.fields.description}</p>
                 <p class="text-xl font-bold text-black mb-2">
                   Price: ${item.fields.price}
                 </p>
               </div>
               <div class="flex justify-start gap-2 mt-2">
                 <a
                   href="/edit-product/${item.pk}"
                   class="flex items-center justify-center w-10 h-10 bg-yellow-500 hover:bg-yellow-600 rounded-full shadow-md transition duration-300"
                 >
                   <svg
                     xmlns="http://www.w3.org/2000/svg"
                     class="w-6 h-6 text-white"
                     viewBox="0 0 20 20"
                     fill="currentColor"
                   >
                     <path
                       d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"
                     />
                   </svg>
                 </a>
                 <a
                   href="/delete/${item.pk}"
                   class="flex items-center justify-center w-10 h-10 bg-red-500 hover:bg-red-600 rounded-full shadow-md transition duration-300"
                 >
                   <svg
                     xmlns="http://www.w3.org/2000/svg"
                     class="w-6 h-6 text-white"
                     viewBox="0 0 20 20"
                     fill="currentColor"
                   >
                     <path
                       fill-rule="evenodd"
                       d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                       clip-rule="evenodd"
                     />
                   </svg>
                 </a>
               </div>
             </div>
 
             `;
         });
     }
     document.getElementById("product_entry_cards").className = classNameString;
     document.getElementById("product_entry_cards").innerHTML = htmlString;
   }
   refreshProductEntries();
   ```
**2. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.**
- 
