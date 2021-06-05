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
- pyhton 3
- Django 3.0.8
- pip 21.1.1
- Pillow 6.2.1 - 6.2.2 keatas
- Web Browser

## Plugins
- Django-import-export 2.5.0
- Django-filter 2.4.0
- Django-crispy-forms 1.11.2
- Django-datetime-widget2 0.9.5
- Django-utils-six

## Installasi
- Buka folder TubesPBO dari sourcecode-editor

## Catatan
Sebelum install django dan pluginnya pastikan bahwa pip dan pillow-nya berada pada versi terbaru
| Plugin | Command |
| ------ | ------ |
|Install/Upgrage Pip | python -m pip install --upgrade pip
|Install/Upgrade Pillow | python -m pip install --upgrade Pillow

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
| Django-datetime-widget2 | pip install django-datetime-widget2 |
| django-utils-six | pip install django-utils-six |

- Migrasi seluruh model/database
```sh
python manage.py makemigrations
python manage.py migrate
```

- Membuat superuser (admin)
```sh
python manage.py createsuperuser
```

- Jalankan Server Django
```sh
python manage.py runserver
```
