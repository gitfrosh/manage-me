from django.forms import *
from manageme.models import *

__author__ = 'Ulrike'

class KundeForm(ModelForm):
      class Meta:
          model = Kunde
          labels = {
              'kname': 'Name',
              'kid': 'ID',
          }
          fields = '__all__'


class ServiceForm(ModelForm):
      class Meta:
          model = Dienstleistungsart
          labels = {
              'dname': 'Dienstleistung',
              'did': 'ID',
          }
          fields = '__all__'

class AuftragForm(ModelForm):
    class Meta:
        model = Auftrag
        labels = {
              'aupload': 'Angebot hochladen!',
              'did': 'Dienstleistung auswaehlen',
              'rid': 'Rechnung auswaehlen',
              'kid': 'Kunde auswaehlen'
          }
        fields = ['aupload', 'did', 'rid', 'kid']

class RechnungForm(ModelForm):
    class Meta:
        model = Rechnung
        labels = {
              'rnummer': 'Eigene Rechnungsnummer angeben!',
              'rdatum': 'Rechnungsdatum',
              'rupload': 'Rechnung hochladen!',
          }
        fields = '__all__'

