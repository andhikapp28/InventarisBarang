# Generated by Django 3.0.8 on 2021-06-05 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_peminjamandetailhistory_tgl_perubahan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjamandetailhistory',
            name='Kondisi',
            field=models.CharField(choices=[('Bagus', 'Bagus'), ('Rusak', 'Rusak')], max_length=10, null=True),
        ),
    ]
