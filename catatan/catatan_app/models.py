from django.db import models
from django.utils import timezone

class Catatan(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal = models.DateTimeField(default=timezone.now)
