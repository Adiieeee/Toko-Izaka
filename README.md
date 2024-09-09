# Tugas 2 PBP
## Link Aplikasi PWS -> [LINKS 🔗](http://muhammad-adiansyah-tokoizakaa.pbp.cs.ui.ac.id/)
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
1. Membuat sebuah proyek Django baru.
   a. Buat direktori baru dengan nama 'toko-izaka' dan masuk ke dalamnya.
   b. Di dalam direktori tersebut, buka command prompt (Windows)
   c. Buat virtual environment 'python -m venv env'
   d. aktifkan virtual environment 'env\Scripts\activate'
   e. Di dalam direktori yang sama, buat berkas 'requirements.txt' dan tambahkan beberapa dependencies.
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```
   f. Lakukan instalasi terhadap dependencies 'pip install -r requirements.txt'
   g. Buat proyek Django bernama 'toko_izaka' dengan perintah 'django-admin startproject toko_izaka .'
   h. Tambahkan 'ALLOWED_HOSTS = ["localhost", "127.0.0.1"]' di 'settings.py'
