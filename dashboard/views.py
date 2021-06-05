from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filter import *
from django.views.generic import View

### Untuk Cetak
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

############### PEGAWAI ###############
@login_required
def pegawai(request):
    items = Pegawai.objects.all()
     #items = Pegawai.objects.raw(' SELECT * FROM dashboard_barang')
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-pegawai')
    else:
        form = PegawaiForm()

    context = {
        'items' : items,
        'form' : form,
    }

    return render(request, 'dashboard/pegawai.html', context)   


############################## BARANG #############################
@login_required
def barang(request):
    items = Barang.objects.all()
    if request.method == 'POST':
        form = BarangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-barang')
    else:
        form = BarangForm()
    context = {
        'items' : items,
        'form' : form,
    }

    return render(request, 'dashboard/barang.html', context)

@login_required
def barang_staff(request):
    items = Barang.objects.all()
    if request.method == 'POST':
        form = BarangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-barang-staff')
    else:
        form = BarangForm()
    context = {
        'items' : items,
        'form' : form,
    }

    return render(request, 'dashboard/barang_staff.html', context)
def hapus_barang(request, pk):
    item = Barang.objects.get(Kode_Barang=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-barang')
    return render(request, 'dashboard/hapus_barang.html')

def update_barang(request, pk):
    item = Barang.objects.get(Kode_Barang=pk)
    if request.method=='POST' :
        form = BarangForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-barang')
    else:
        form = BarangForm(instance=item)
    context ={
        'form':form
    }
    return render(request, 'dashboard/update_barang.html', context)

def BAST_Barang(request, pk):
    item = Barang.objects.get(Kode_Barang=pk)
    context = {
        'item' : item.BAST
    }
    return render(request, 'dashboard/BAST_Barang.html', context)

def BAST_BarangStaff(request, pk):
    item = Barang.objects.get(Kode_Barang=pk)
    context = {
        'item' : item.BAST
    }
    return render(request, 'dashboard/BAST_BarangStaff.html', context)

################## GEDUNG #######################
@login_required
def gedung(request):
    items = Gedung.objects.all()
    if request.method == 'POST':
        form = GedungForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-gedung')
    else:
        form = GedungForm()
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request, 'dashboard/gedung.html', context)

def hapus_gedung(request, pk):
    item = Gedung.objects.get(Nama_Gedung=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-gedung')
    return render(request, 'dashboard/hapus_gedung.html')

def update_gedung(request, pk):
    item = Gedung.objects.get(Nama_Gedung=pk)
    if request.method=='POST' :
        form = GedungForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-gedung')
    else:
        form = GedungForm(instance=item)
    context ={
        'form':form
    }
    return render(request, 'dashboard/update_gedung.html', context)    

########################### RUANG #####################
@login_required
def ruang(request):
    items = Ruang.objects.all()
    if request.method == 'POST':
        form = RuangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-ruang')
    else:
        form = RuangForm()
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request, 'dashboard/ruang.html', context)

def hapus_ruang(request, pk):
    item = Ruang.objects.get(Ruang=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-ruang')
    return render(request, 'dashboard/hapus_ruang.html')

def update_ruang(request, pk):
    item = Ruang.objects.get(Ruang=pk)
    if request.method=='POST' :
        form = RuangForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-ruang')
    else:
        form = RuangForm(instance=item)
    context ={
        'form':form
    }
    return render(request, 'dashboard/update_ruang.html', context)  

############################# PEMINJAMAN ############################
@login_required
def peminjaman(request):
    items = Peminjaman.objects.all()
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-peminjaman')
    else:
        form = PeminjamanForm()
    
    if request.method == 'GET':
        items = Peminjaman.objects.all()
        cari = CariPeminjamanForm(request.GET or None)
        myFilter = CariPeminjaman(request.GET, queryset=items)
        items = myFilter.qs

    context = {
        'items' : items,
        'form' : form,
        'cari' : cari,
    }
    return render(request, 'dashboard/peminjaman.html', context)

def hapus_peminjaman(request, pk):
    item = Peminjaman.objects.get(No_Peminjaman=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-peminjaman')
    return render(request, 'dashboard/hapus_peminjaman.html')

def update_peminjaman(request, pk):
    item = Peminjaman.objects.get(No_Peminjaman=pk)
    if request.method=='POST' :
        form = PeminjamanForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-peminjaman')
    else:
        form = PeminjamanForm(instance=item)
    context ={
        'form':form
    }
    return render(request, 'dashboard/update_peminjaman.html', context)  

def BAST_Peminjaman(request, pk):
    item = Peminjaman.objects.get(No_Peminjaman=pk)
    context = {
        'item' : item.BAST
    }
    return render(request, 'dashboard/BAST_Peminjaman.html', context) 



#################################################
@login_required
def peminjamandetail(request):
    items = PeminjamanDetail.objects.all()
    if request.method == 'POST':
        form = PeminjamanDetailForm(request.POST, request.FILES)
        history = PeminjamanDetailHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            history.form=form
            history.save()
            return redirect('dashboard-peminjamandetail')
    else:
        form = PeminjamanDetailForm()
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request, 'dashboard/peminjamandetail.html', context)

@login_required
def peminjamandetailhistory(request):
    items = PeminjamanDetailHistory.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/peminjamandetailhistory.html', context)

def update_peminjamandetail(request, pk):
    item = PeminjamanDetail.objects.get(No_Peminjaman=pk)
    if request.method=='POST' :
        form = PeminjamanDetailForm(request.POST, instance=item)
        history = PeminjamanDetailHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            history.form=form
            history.save()
            return redirect('dashboard-peminjamandetail')
    else:
        form = PeminjamanDetailForm(instance=item)
    context ={
        'form':form
    }
    return render(request, 'dashboard/update_peminjamandetail.html', context)


#####################################################
@login_required
def cetak_laporan(request):
    items = PeminjamanDetail.objects.all()
    form = CetakLaporanForm(request.POST or None)
    myFilter = CariBarang(request.POST, queryset=items)
    items = myFilter.qs
    context = {
        'form' : form,
        'items' : items,
        'myFilter' : myFilter,
    }
    return render(request, 'dashboard/cetak_laporan.html', context)

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        items = PeminjamanDetail.objects.all()
        myFilter = CariBarang(request.POST, queryset=items)
        items = myFilter.qs
        context = {
        'items' : items,
        'myFilter' : myFilter,
    }
        pdf = render_to_pdf('dashboard/cetak_laporan.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
