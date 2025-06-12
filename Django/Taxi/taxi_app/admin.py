from django.contrib import admin
from taxi_app.models import PinTaxiAvailable, TaxiOnRunning

# Register your models here.
admin.site.register(PinTaxiAvailable)
admin.site.register(TaxiOnRunning)