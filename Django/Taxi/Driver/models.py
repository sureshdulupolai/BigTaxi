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
    DriverTotalTripCount = models.CharField(max_length=10)

    def __str__(self):
        return str((self.VUDM.ULink.username, self.DriverStatus))