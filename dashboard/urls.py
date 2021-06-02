from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    
    path('pegawai/', views.pegawai, name='dashboard-pegawai'),
    
    path('barang/', views.barang, name='dashboard-barang'),
    path('barang/hapus/<str:pk>/', views.hapus_barang, name='dashboard-hapus-barang'),
    path('barang/update/<str:pk>/', views.update_barang, name='dashboard-update-barang'),
    path('barang/bast/<str:pk>/', views.BAST_Barang, name='dashboard-bast-barang'),
    
    path('gedung/', views.gedung, name='dashboard-gedung'),
    path('gedung/hapus/<str:pk>/', views.hapus_gedung, name='dashboard-hapus-gedung'),
    path('gedung/update/<str:pk>/', views.update_gedung, name='dashboard-update-gedung'),
    
    path('ruang/', views.ruang, name='dashboard-ruang'),
    path('ruang/hapus/<str:pk>/', views.hapus_ruang, name='dashboard-hapus-ruang'),
    path('ruang/update/<str:pk>/', views.update_ruang, name='dashboard-update-ruang'),
    
    path('peminjaman/', views.peminjaman, name='dashboard-peminjaman'),
    path('peminjaman/hapus/<str:pk>/', views.hapus_peminjaman, name='dashboard-hapus-peminjaman'),
    path('peminjaman/update/<str:pk>/', views.update_peminjaman, name='dashboard-update-peminjaman'),
    path('peminjaman/bast/<str:pk>/', views.BAST_Peminjaman, name='dashboard-bast-peminjaman'),
    
    path('peminjamandetail/', views.peminjamandetail, name='dashboard-peminjamandetail'),
    path('peminjamandetail/update/<str:pk>/', views.update_peminjamandetail, name='dashboard-update-peminjamandetail'),

    path('laporan/', views.cetak_laporan, name='dashboard-cetak-laporan'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


