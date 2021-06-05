from django.db import models

# Create your models here.

class Barang(models.Model):
    ID = models.PositiveIntegerField()
    Kode_Barang = models.CharField(max_length=6, primary_key=True)
    Nama_Barang = models.CharField(max_length=30, null=True)
    Merk = models.CharField(max_length=30, null=True)
    Stock = models.PositiveIntegerField(null=True)
    BAST = models.FileField(("BAST Perolehan"), upload_to=None, max_length=100)

    def __str__(self):
        return f'{self.Kode_Barang}-{self.Nama_Barang}'

class Pegawai(models.Model):
    NIP_NRK = models.CharField(max_length=20, primary_key=True)
    Nama_Pegawai = models.CharField(max_length=30)
    Alamat = models.CharField(max_length=100)
    Telp = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.NIP_NRK} - {self.Nama_Pegawai}'
    
class Gedung(models.Model):
    ID = models.PositiveIntegerField()
    Nama_Gedung = models.CharField(max_length=20, primary_key=True)
    MG = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.Nama_Gedung}'
    
class Ruang(models.Model):
    ID = models.PositiveIntegerField()
    Ruang = models.CharField(max_length=20, primary_key=True)
    PJ_Ruang = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL)
    Gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Ruang}-{self.Gedung}'

class Peminjaman (models.Model):
    ID = models.PositiveIntegerField()
    No_Peminjaman = models.CharField(max_length=10, primary_key=True)
    NIP_NRK = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    tgl_pinjam = models.DateTimeField(auto_now_add=True)
    tgl_kembali = models.DateTimeField(null=True, blank=True)
    BAST = models.FileField(("BAST Disposisi"), upload_to=None, max_length=100)

    def __str__(self):
        return f'{self.No_Peminjaman}'

Pilihan_Kondisi =  (('Bagus','Bagus'),('Rusak','Rusak'))
class PeminjamanDetail(models.Model):
    No_Peminjaman = models.OneToOneField(Peminjaman, on_delete=models.CASCADE)
    Kode_Barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    Kondisi = models.CharField(max_length=10, choices=Pilihan_Kondisi, null=True)
    Jumlah = models.PositiveIntegerField()
    Gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)
    Ruang = models.ForeignKey(Ruang, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.No_Peminjaman}'

class PeminjamanDetailHistory(models.Model):
    No_Peminjaman = models.CharField(max_length=10 ,null=True, blank=True)
    Kode_Barang = models.CharField(max_length=10, null=True, blank=True)
    Kondisi = models.CharField(max_length=10, null=True)
    Jumlah = models.PositiveIntegerField()
    Gedung = models.CharField(max_length=10 ,null=True, blank=True)
    Ruang = models.CharField(max_length=10, null=True, blank=True,)
    tgl_perubahan = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.No_Peminjaman}'

