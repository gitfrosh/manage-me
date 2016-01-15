from django.contrib import admin
from manageme.models import *

# Register your models here.

admin.site.register(Kunde)
admin.site.register(Dienstleistungsart)
admin.site.register(Rechnung)
admin.site.register(Auftrag)