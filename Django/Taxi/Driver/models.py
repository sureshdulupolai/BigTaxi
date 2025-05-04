from django.db import models
from Users.models import usersDataModel

# Create your models here.
class driverDataModel(models.Model):
    VUDM = models.ForeignKey(usersDataModel, on_delete=models.CASCADE)
    VehicleName = models.CharField(max_length=200)
    VehicleCustomerLimit = models.CharField(max_length=10)
    Vehicle = models.CharField(max_length=100)
    VehicleNo = models.CharField(max_length=100)
    DriverStatus = models.CharField(max_length=20, default='active')
    DriverTotalTripCount = models.IntegerField(max_length=10, default=0)

    def __str__(self):
        return str((self.DriverStatus))