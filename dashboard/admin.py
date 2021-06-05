from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib.auth.models import Group


admin.site.site_header = 'TUBES PBO'
class BarangAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('Kode_Barang', 'Nama_Barang', 'Stock', 'BAST')

class GedungAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('ID', 'Nama_Gedung', 'MG')

class PegawaiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('NIP_NRK', 'Nama_Pegawai', 'Alamat', 'Telp')

class RuangAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('ID', 'Ruang', 'PJ_Ruang', 'Gedung')

class PeminjamanAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('ID', 'No_Peminjaman', 'NIP_NRK', 'tgl_pinjam','tgl_kembali', 'BAST')

class PeminjamanDetailAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('No_Peminjaman', 'Kode_Barang', 'Kondisi', 'Jumlah', 'Gedung', 'Ruang')

class PeminjamanDetailHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('No_Peminjaman', 'Kode_Barang', 'Kondisi', 'Jumlah', 'Gedung', 'Ruang', 'tgl_perubahan')
# Register Models
admin.site.register(Barang, BarangAdmin)
admin.site.register(Pegawai, PegawaiAdmin)
admin.site.register(Gedung, GedungAdmin)
admin.site.register(Ruang, RuangAdmin)
admin.site.register(Peminjaman, PeminjamanAdmin)
admin.site.register(PeminjamanDetail, PeminjamanDetailAdmin)
admin.site.register(PeminjamanDetailHistory, PeminjamanDetailHistoryAdmin)
#admin.site.unregister(Group)