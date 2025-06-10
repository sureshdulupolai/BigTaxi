from django.db import models
from Users.models import usersDataModel

# Create your models here.
class TaxiBarCode(models.Model):
    barCode = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

class PinTaxiAvailable(models.Model):
    run = [('not', 'not'),('yes', 'yes')]
    taxiAvaId = models.CharField(max_length=50)
    taxiCity = models.CharField(max_length=500)
    customerId = models.ForeignKey(usersDataModel, on_delete=models.CASCADE)
    currentLocation = models.CharField(max_length=2000)
    toLocation = models.CharField(max_length=2000, default='No Area Found!')
    taxiPassenger = models.IntegerField(default=1)
    pincode = models.CharField(max_length=20, default=' ')
    couponCodeWas = models.CharField(max_length=100, default='Customer Not Have Coupon')
    taxiDate = models.DateField(auto_now_add=True)
    taxiTime = models.TimeField(auto_now_add=True)
    taxiDateAndTimeByUser = models.CharField(max_length=100, default='none')
    priceOfTravel = models.IntegerField(default=0)
    driverCode = models.CharField(max_length=100, default='DRIVERCODE')
    runningStatus = models.CharField(max_length=100, choices=run, default='not')
    
    def __str__(self):
        return str((self.taxiAvaId, self.taxiDate ,self.taxiTime))
    
class TaxiTimeOver(models.Model):
    # success or failed
    statusOfTaxiData = [('Success', 'Success'),('Failed', 'Failed')]

    toTaxiAvaId = models.CharField(max_length=50)
    taxiCityAndLoc = models.CharField(max_length=2100)
    avaPincode = models.CharField(max_length=20, default=' ')
    dateAndTime = models.CharField(max_length=100)
    toDate = models.DateField(auto_now_add=True)
    toTime = models.TimeField(auto_now_add=True)
    toDriverName = models.CharField(max_length=500)
    toStatus = models.CharField(choices=statusOfTaxiData, default='Failed')

    def __str__(self):
        return str((self.toDriverName, self.toTaxiAvaId, self.toStatus))
    
class TaxiOnFinish(models.Model):
    statusCode = models.CharField(max_length=50)
    taxiDriver = models.CharField(max_length=500)
    taxiCustomer = models.CharField(max_length=500)
    totalPassanger = models.CharField(max_length=10)
    taxiFrom = models.CharField(max_length=4000)
    taxiTo = models.CharField(max_length=4000)
    taxiStartTime = models.CharField(max_length=100)
    taxiFinishTime = models.TimeField(auto_now_add=True)
    taxiDate = models.DateField(auto_now_add=True)
    fairPrice = models.CharField(max_length=40)
    cuponCode = models.CharField(max_length=100, default='none')
    fairTaxiPriceTaken = models.CharField(max_length=40)
    driverReview = models.CharField(max_length=5000)
    driverRating = models.IntegerField()

    def __str__(self):
        return str((self.statusCode, self.taxiDate))
    
class PaymentManagement(models.Model):
    statusCode = models.CharField(max_length=50)
    fairTaken = models.CharField(max_length=20)
    dateOfFairTaken = models.DateField(auto_now_add=True)
    timeOfFairTaken = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str((self.fairTaken, self.dateOfFairTaken))
    
class FinishReviewByCustomer(models.Model):
    statusCode = models.CharField(max_length=50)
    customerReview = models.CharField(max_length=5000, default='')
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.statusCode
    
class TaxiOnRunning(models.Model):
    statusCode = models.CharField(max_length=50)
    taxiDriverName = models.CharField(500)
    taxiCustomerName = models.CharField(max_length=500)
    totalPassanger = models.CharField(max_length=10)
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
    totalPassanger = models.CharField(max_length=10)
    fairPrice = models.CharField(max_length=40)
    taxiFrom = models.CharField(max_length=4000)
    taxiTo = models.CharField(max_length=4000)
    onCancelArea = models.CharField(max_length=4000)
    review = models.CharField(max_length=5000)
    cancelImage = models.ImageField(upload_to='cancelReportImage/Report/', default='cancelReportImage/default/default.jpeg')

    def __str__(self):
        # Try ( self.cancelImage.name != '' )
        if self.cancelImage != 'cancelReportImage/default/default.jpeg':
            return str((self.statusCode, 'Image'))
        else:
            return str((self.statusCode, 'No Image'))

# Management Feild Of Big Taxi
# -----------------------------------------------------------------------------------------------------------------
class ManagementModel(models.Model):
    totalFairPrice = models.CharField(max_length=1000)
    totalAmountTakenByUs = models.CharField(max_length=1000)
    totalAmountShouldBeReturn = models.CharField(max_length=1000)
    totalTripCount = models.CharField(max_length=30)
    monthOfTotal = models.CharField(max_length=50)
    yearOfTotal = models.CharField(max_length=5)
    dateOfChecking = models.DateField(auto_now_add=True)
    timeOfChecking = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str((self.monthOfTotal, self.totalFairPrice, self.totalTripCount))