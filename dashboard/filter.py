import django_filters
from .models import *

class CariBarang(django_filters.FilterSet):
    class Meta:
        model = PeminjamanDetail
        fields = ['Gedung', 'Ruang']

class CariRuang(django_filters.FilterSet):
    class Meta:
        model = Ruang
        fields = ['Ruang']

class CariPeminjaman(django_filters.FilterSet):
    class Meta:
        model = Peminjaman
        fields = ['No_Peminjaman']

class CariPeminjamanHistory(django_filters.FilterSet):
    class Meta:
        model = PeminjamanDetailHistory
        fields = ['No_Peminjaman']