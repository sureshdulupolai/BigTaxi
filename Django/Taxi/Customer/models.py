from django.db import models
from Users.models import usersDataModel

# Create your models here.
class cutomerDataModel(models.Model):
    UDM = models.ForeignKey(usersDataModel, on_delete=models.CASCADE)
    totalTripCount = models.IntegerField(default=0)
    userName = models.CharField(max_length=100, default='Big Taxi User')
    userImage = models.ImageField(default='customer/default/logo.png', upload_to='customer/exist/', max_length=1000)
    description = models.CharField(max_length=2000, default='No Description!')
    
    def __str__(self):
        return str((self.UDM, self.totalTripCount))