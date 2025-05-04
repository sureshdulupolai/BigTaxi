from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class usersDataModel(models.Model):
    UserG = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Not Check', 'Not Check'),
    ]
    
    UserC = [
        ('Developer', 'Developer'),
        ('Customer', 'Customer'),
        ('Driver', 'Driver'),
    ]

    ULink = models.ForeignKey(User, on_delete=models.CASCADE)
    UserCategory = models.CharField(choices=UserC, default='Customer')
    UserMobileNo = models.CharField(max_length=11)
    UserGender = models.CharField(max_length=100, default='Not Check')
    UserAge = models.CharField(max_length=3, default='')
    UserState = models.CharField(max_length=100, default='')
    UserCity = models.CharField(max_length=100, default='')
    UserPincode = models.CharField(max_length=20, default='')
    UserAddress = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.UserMobileNo)