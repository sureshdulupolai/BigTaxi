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

    def __str__(self):
        return str((self.DriverStatus))
    
class driveDataStore(models.Model):
    DriverTotalTripCount = models.IntegerField(default=0)
    driver = models.ForeignKey(usersDataModel, on_delete=models.CASCADE)

    def __str__(self):
        return str((self.driver.ULink.username))
    
# for ID Checking
class DriverModelStore(models.Model):
    CouponCode = models.CharField(max_length=50)
    DriverName = models.CharField(max_length=1000)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str((self.CouponCode, self.DriverName))