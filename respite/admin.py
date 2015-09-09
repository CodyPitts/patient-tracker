from django.contrib import admin
from .models import FAQ, Patient, Visit

admin.site.register(FAQ)
admin.site.register(Patient)
admin.site.register(Visit)