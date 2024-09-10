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
   10. Buatlah repositori GitHub baru bernama `toko-izaka`
   11. Jalankan apa yang ada di Github pada cmd yang mengarah pada direktori lokal untuk menyambungkan
   12. Tambahkan berkas `.gitignore` dengan isi
       ```
       # Django
       *.log
       *.pot
       *.pyc
       __pycache__
       db.sqlite3
       media
      
       # Backup files
       *.bak
      
       # If you are using PyCharm
       # User-specific stuff
       .idea/**/workspace.xml
       .idea/**/tasks.xml
       .idea/**/usage.statistics.xml
       .idea/**/dictionaries
       .idea/**/shelf
      
       # AWS User-specific
       .idea/**/aws.xml
      
       # Generated files
       .idea/**/contentModel.xml
       .DS_Store
      
       # Sensitive or high-churn files
       .idea/**/dataSources/
       .idea/**/dataSources.ids
       .idea/**/dataSources.local.xml
       .idea/**/sqlDataSources.xml
       .idea/**/dynamic.xml
       .idea/**/uiDesigner.xml
       .idea/**/dbnavigator.xml
      
       # Gradle
       .idea/**/gradle.xml
       .idea/**/libraries
      
       # File-based project format
       *.iws
      
       # IntelliJ
       out/
      
       # JIRA plugin
       atlassian-ide-plugin.xml
      
       # Python
       *.py[cod]
       *$py.class
      
       # Distribution / packaging
       .Python build/
       develop-eggs/
       dist/
       downloads/
       eggs/
       .eggs/
       lib/
       lib64/
       parts/
       sdist/
       var/
       wheels/
       *.egg-info/
       .installed.cfg
       *.egg
       *.manifest
       *.spec
      
       # Installer logs
       pip-log.txt
       pip-delete-this-directory.txt
      
       # Unit test / coverage reports
       htmlcov/
       .tox/
       .coverage
       .coverage.*
       .cache
       .pytest_cache/
       nosetests.xml
       coverage.xml
       *.cover
       .hypothesis/
      
       # Jupyter Notebook
       .ipynb_checkpoints
      
       # pyenv
       .python-version
      
       # celery
       celerybeat-schedule.*
      
       # SageMath parsed files
       *.sage.py
      
       # Environments
       .env
       .venv
       env/
       venv/
       ENV/
       env.bak/
       venv.bak/
      
       # mkdocs documentation
       /site
      
       # mypy
       .mypy_cache/
      
       # Sublime Text
       *.tmlanguage.cache
       *.tmPreferences.cache
       *.stTheme.cache
       *.sublime-workspace
       *.sublime-project
      
       # sftp configuration file
       sftp-config.json
      
       # Package control specific files Package
       Control.last-run
       Control.ca-list
       Control.ca-bundle
       Control.system-ca-bundle
       GitHub.sublime-settings
      
       # Visual Studio Code
       .vscode/*
       !.vscode/settings.json
       !.vscode/tasks.json
       !.vscode/launch.json
       !.vscode/extensions.json
       .history
       ```
   13. Lakukan `add`, `commit`, dan `push` dari direktori repositori lokal.
   14. aktifkan virtual environment `env\Scripts\activate`
   15. membuat aplikasi baru dengan nama `main` dengan perintah `python manage.py startapp main`
   16. Buka berkas `settings.py` di dalam direktori proyek `toko_izaka`, tambahkan `main` ke dalam daftar aplikasi pada variabel `INSTALLED_APPS`
   17. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`
   18. Di dalam direktori `templates`, buat berkas baru bernama `main.html`. Isi berkas `main.html` dengan kode html sesuai keinginan mu dan dapat dibuat sebaik mungkin.
   19. Buka berkas `models.py` pada direktori aplikasi `main` dan isi dengan
       ```
       from django.db import models

       class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.IntegerField()
          description = models.TextField()
       ```
   20. Jalankan perintah berikut untuk membuat migrasi model `python manage.py makemigrations`
   21. Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal. `python manage.py migrate`
   22. Buka berkas `views.py` yang terletak di dalam berkas aplikasi `main` lalu tambahkan fungsi `show_main`.
       ```
       from django.shortcuts import render

       def show_main(request):
           context = {
               'name' : 'Phantom Mask',
               'image' : 'https://imgur.com/a/U0fYFir',
               'price': '700000',
               'description': 'A mysterious Mask found in the depth of mountains, legend said that this mask once belong the the monkey king itself'
           }

       return render(request, "main.html", context)
       ```
   23. Buka berkas `main.html` lalu ubah kodenya menjadi struktur kode Django yang sesuai untuk menampilkan data.
   24. Buatlah berkas `urls.py` di dalam direktori `main` lalu isi dengan kode ini
       ```
       from django.urls import path
       from main.views import show_main
      
       app_name = 'main'
      
       urlpatterns = [
           path('', show_main, name='show_main'),
       ]
       ```
   25. Buka berkas `urls.py` di dalam direktori proyek `toko_izaka`
   26. Impor fungsi `include` dari `django.urls`.
   27. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
       ```
       urlpatterns = [
           ...
           path('', include('main.urls')),
           ...
       ]
       ```
   28. Lakukan `add`, `commit`, dan `push` dari direktori repositori lokal.
   29. Akses halaman PWS pada https://pbp.cs.ui.ac.id.
   30. Buat proyek baru dengan menekan tombol `Create New Project`
   31. isi `Project Name` dengan `toko-izakaa`. Setelah itu, tekan `Create New Project`
   32. Pada `settings.py` di proyek Django yang sudah kamu buat tadi, tambahkan URL deployment PWS pada `ALLOWED_HOSTS`
   33. Langkah ini perlu kamu lakukan agar proyek Django kamu dapat diakses melalui URL deployment PWS. Lakukan `git add`, `commit`, dan `push` perubahan ini ke repositori GitHub kamu.
   34. Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS, tunggu hingga kelar building lalu bisa pencet tombol `view project`
