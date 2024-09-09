# Tugas 2 PBP
## Link Aplikasi PWS -> [LINKS 🔗](http://muhammad-adiansyah-tokoizakaa.pbp.cs.ui.ac.id/)
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
#### Membuat sebuah proyek Django baru.
   1. Buat direktori baru dengan nama 'toko-izaka' dan masuk ke dalamnya.
   2. Di dalam direktori tersebut, buka command prompt (Windows)
   3. Buat virtual environment 'python -m venv env'
   4. aktifkan virtual environment 'env\Scripts\activate'
   5. Di dalam direktori yang sama, buat berkas 'requirements.txt' dan tambahkan beberapa dependencies.
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```
   6. Lakukan instalasi terhadap dependencies 'pip install -r requirements.txt'
   7. Buat proyek Django bernama 'toko_izaka' dengan perintah 'django-admin startproject toko_izaka .'
   8. Tambahkan 'ALLOWED_HOSTS = ["localhost", "127.0.0.1"]' di 'settings.py'
