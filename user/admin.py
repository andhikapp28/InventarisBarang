from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Profile)
