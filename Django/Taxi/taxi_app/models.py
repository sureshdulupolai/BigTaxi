from django.db import models
from Users.models import usersDataModel

# Create your models here.
class TaxiAvailable(models.Model):
    taxiAvaId = models.CharField(max_length=50)
    taxiCity = models.CharField(max_length=500)
    diverId = models.ForeignKey(usersDataModel, on_delete=models.CASCADE)
    currentLocation = models.CharField(max_length=2000)
    pincode = models.CharField(max_length=20, default=' ')
    taxiDate = models.DateField()
    taxiTime = models.TimeField()

    def __str__(self):
        return str((self.taxiAvaId, self.taxiDate ,self.taxiTime))
    
class TaxiTimeOver(models.Model):
    # success or failed
    statusOfTaxiData = [('Success', 'Success'),('Failed', 'Failed')]

    toTaxiAvaId = models.CharField(max_length=50)
    taxiCityAndLoc = models.CharField(max_length=2100)
    avaPincode = models.CharField(max_length=20, default=' ')
    dateAndTime = models.CharField(max_length=100)
    toDate = models.DateField()
    toTime = models.TimeField()
    toDriverName = models.CharField(max_length=500)
    toStatus = models.CharField(choices=statusOfTaxiData, default='Failed')

    def __str__(self):
        return str((self.toDriverName, self.toTaxiAvaId, self.toStatus))
    
class TaxiOnFinish(models.Model):
    statusCode = models.CharField(max_length=50)
    taxiDriver = models.CharField(max_length=500)
    taxiCustomer = models.CharField(max_length=500)
    taxiFrom = models.CharField(max_length=4000)
    taxiTo = models.CharField(max_length=4000)
    taxiStartTime = models.CharField(max_length=100)
    taxiFinishTime = models.TimeField()
    taxiDate = models.DateField()
    fairPrice = models.CharField(max_length=40)
    cuponCode = models.CharField(max_length=100, default='none')
    fairTaxiPriceTaken = models.CharField(max_length=40)

    def __str__(self):
        return str((self.statusCode, self.taxiDate))
    
class TaxiOnRunning(models.Model):
    statusCode = models.CharField(max_length=50)
    taxiDriverName = models.CharField(500)
    taxiCustomerName = models.CharField(max_length=500)
    taxiRunningFrom = models.CharField(max_length=4000)
    taxiRunningTo = models.CharField(max_length=4000)
    taxiStartTime = models.CharField(max_length=100)
    taxiFutureEndTime = models.CharField(max_length=100)
    taxiFairPrice = models.CharField(max_length=40)
    cuponCode = models.CharField(max_length=100, default='none')

    def __str__(self):
        return str((self.statusCode, self.taxiDriverName, self.taxiCustomerName))
    
class TaxiOnCancel(models.Model):
    statusCode = models.CharField(max_length=100)
    DriverName = models.CharField(max_length=500)
    CustomerName = models.CharField(max_length=500)
    fairPrice = models.CharField(max_length=40)
    taxiFrom = models.CharField(max_length=4000)
    taxiTo = models.CharField(max_length=4000)
    onCancelArea = models.CharField(max_length=4000)
    review = models.CharField(max_length=5000)
    cancelImage = models.ImageField(upload_to='cancelReportImage/Report/', default='cancelReportImage/default/default.jpg')

    def __str__(self):
        if self.cancelImage.name != 'cancelReportImage/default/default.jpg':
            return str((self.statusCode, 'Image'))
        else:
            return str((self.statusCode, 'No Image'))
