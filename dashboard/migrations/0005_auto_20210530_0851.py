# Generated by Django 3.0.8 on 2021-05-30 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210530_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gedung',
            old_name='MG',
            new_name='MG_Gedung',
        ),
    ]