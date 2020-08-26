from django.contrib import admin
from .models import Catatan

class CatatanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')

admin.site.register(Catatan, CatatanAdmin)

# user = admin
# pass = passsementara