from django.db import models
from Users.models import usersDataModel

class PinDeleteReview(models.Model):
    dataLike = [('report', 'report'),('normal', 'normal')]

    deleteType = models.CharField(choices=dataLike, default='normal', max_length=15)
    pinBarCode = models.CharField(max_length=100)
    userBarCode = models.CharField(max_length=100)
    driverCode = models.CharField(max_length=100, default='DRIVERCODE')
    review = models.CharField(max_length=100, default='No Report, Delete By User')
    addressFrom = models.CharField(max_length=5000)
    addressTo = models.CharField(max_length=5000)
    date_Time = models.CharField(max_length=100)
    passenger = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default='No Price')
    discountCoupon = models.CharField(max_length=100, default='Customer Not Have Coupon')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"AvaId : {self.pinBarCode}, Customer : {self.userBarCode}, Driver : {self.driverCode}"