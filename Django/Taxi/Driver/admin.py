from django.contrib import admin
from Driver.models import driverDataModel, DriverAcceptedPin, ReportDriverInPinTaxi

# Register your models here.
admin.site.register(driverDataModel)
admin.site.register(DriverAcceptedPin)
admin.site.register(ReportDriverInPinTaxi)