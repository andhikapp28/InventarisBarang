from django import forms
from .models import *
from datetimewidget.widgets import DateTimeWidget

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['ID', 'Kode_Barang', 'Nama_Barang', 'Merk', 'Stock', 'BAST']

class PegawaiForm(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = ['NIP_NRK', 'Nama_Pegawai', 'Alamat', 'Telp']

class GedungForm(forms.ModelForm):
    class Meta:
        model = Gedung
        fields = ['ID', 'Nama_Gedung', 'MG']

class RuangForm(forms.ModelForm):
    class Meta:
        model = Ruang
        fields = ['ID', 'Ruang','PJ_Ruang', 'Gedung']

class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = ['ID', 'No_Peminjaman', 'NIP_NRK', 'tgl_kembali', 'BAST' ]
        widgets = {'tgl_kembali' : DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=4)}   

class PeminjamanDetailForm(forms.ModelForm):
    class Meta:
        model = PeminjamanDetail
        fields = ['No_Peminjaman', 'Kode_Barang', 'Kondisi', 'Jumlah', 'Gedung', 'Ruang']

class PeminjamanDetailHistoryForm(forms.ModelForm):
    class Meta:
        model = PeminjamanDetailHistory
        fields = ['No_Peminjaman', 'Kode_Barang', 'Kondisi', 'Jumlah', 'Gedung', 'Ruang']

class CetakLaporanForm(forms.ModelForm):
    class Meta:
        model = PeminjamanDetail
        fields = ['Gedung', 'Ruang']

class CariPeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = ['No_Peminjaman']

class CariPeminjamanHistoryForm(forms.ModelForm):
    class Meta:
        model = PeminjamanDetailHistory
        fields = ['No_Peminjaman']