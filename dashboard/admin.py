from django.contrib import admin
from .models import Barang, Pegawai, PeminjamanDetail, Peminjaman, Gedung, Ruang
from django.contrib.auth.models import Group

admin.site.site_header = 'TUBES PBO'
class BarangAdmin(admin.ModelAdmin):
    list_display=('Kode_Barang', 'Nama_Barang', 'Stock', 'BAST')
# Register your models here.
admin.site.register(Barang, BarangAdmin)
admin.site.register(Pegawai)
admin.site.register(Gedung)
admin.site.register(Ruang)
admin.site.register(Peminjaman)
admin.site.register(PeminjamanDetail)
#admin.site.unregister(Group)