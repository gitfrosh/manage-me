__author__ = 'Ulrike'

from django.db import models
from django.core.files.base import ContentFile

class Kunde(models.Model):
    kname = models.CharField(max_length=30)
    kid = models.AutoField(primary_key=True)
    adresse = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.kname


class Dienstleistungsart(models.Model):
    dname = models.CharField(max_length=30)
    did = models.AutoField(primary_key=True)

    def __str__(self):
        return self.dname


class Rechnung(models.Model):
    rid = models.AutoField(primary_key=True)
    rnummer = models.CharField(max_length=30)
    rdatum = models.DateField()
    rupload = models.FileField(upload_to='docs/', default='null')


    def __str__(self):
        return self.rnummer


class Auftrag(models.Model):
    aid = models.AutoField(primary_key=True)
    aupload = models.FileField(upload_to='docs/', default='null')
    rid=models.ManyToManyField(Rechnung, blank=True)
    did=models.ManyToManyField(Dienstleistungsart)
    kid=models.ForeignKey(Kunde)

    def __str__(self):
        return self.aid