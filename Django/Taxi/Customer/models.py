from django.db import models
from Users.models import usersDataModel

class PinDeleteReview(models.Model):
    pinBarCode = models.CharField(max_length=100)
    userBarCode = models.CharField(max_length=100)
    driverCode = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    addressFrom = models.CharField(max_length=5000)
    addressTo = models.CharField(max_length=5000)
    date_Time = models.CharField(max_length=100)
    passenger = models.CharField(max_length=100)
    price = models.IntegerField()
    discountCoupon = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"AvaId : {self.pinBarCode}, Customer : {self.userBarCode}, Driver : {self.driverCode}"