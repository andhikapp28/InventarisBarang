# Tugas Besar PBO 2021

Tugas besar PBO membuat inventaris barang lingkungan ITERA
- Django
- Bootstrap

## Fungsi
- Login dan Register
- Melihat/Mengedit Profil Diri Sendiri
- Pegawai
- Menambah Barang (Inventaris)
- Melihat Daftar Peminjaman Yang Telah Dilakukan
- Menambah Ruang Pada Suatu Gedung
- Melihat dan Mengedit Daftar Peminjaman Yang Telah Dilakukan
- Mencetak Laporan


## Aplikasi
- Visual Studio Code atau source code editor lainnya

## Requirement
- Django 3.0.8
- Web Browser

## plugins
- Django-import-export 2.5.0
- Django-filter 2.4.0
- Django-crispy-forms 1.11.2
- Django-datetime-widget 2 0.9.5

## Installasi
- Buka folder TubesPBO dari sourcecode-editor
- Install Django pada sourcecode-editor
```sh
python -m pip install Django
```
- install seluruh plugins

| Plugin | Command |
| ------ | ------ |
| Django-import-export  | pip install django-import-export |
| Django-filter | pip install django-filter |
| Django-crispy-forms | pip install django-crispy-forms |
| Django-datetime-widget | pip install django-datetime-widget |

- Migrasi seluruh model/database
```sh
python manage.py makemigrations
python manage.py migrate
```
- Membuat superuser (admin)
```sh
python manage.py createsuperuser
```

- Jalankan server django
```sh
python manage.py runserver
```



