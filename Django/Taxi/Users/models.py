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
    UserCode = models.CharField(max_length=100, default='BIGTAXICODE1006463')
    UserCategory = models.CharField(choices=UserC, default='Customer', max_length=20)
    UserMobileNo = models.CharField(max_length=11)
    UserGender = models.CharField(max_length=100, default='Not Check')
    UserAge = models.CharField(max_length=3, default='')
    UserState = models.CharField(max_length=100, default='')
    UserCity = models.CharField(max_length=100, default='')
    UserPincode = models.CharField(max_length=20, default='')
    UserAddress = models.CharField(max_length=200, default='')
    UserPass = models.CharField(max_length=1000, default='password')
    CouponCode = models.CharField(max_length=50, null=True, blank=True)
    UProfileImage = models.ImageField(upload_to='profile/main/', default='profile/default/default.png')
    UProfileName = models.CharField(max_length=1000, default='BiXTaxi User')
    description = models.CharField(max_length=5000, default='No Description!')
    totalTripCount = models.IntegerField(default=0)
    dangerTripCount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.UserMobileNo} : {self.UserCategory}"

class ReviewAndRating(models.Model):
    username = models.CharField(max_length=500)
    userCode = models.CharField(max_length=100)
    ratingBarCode = models.CharField(max_length=1000)
    userReview = models.CharField(max_length=5000)
    userStar = models.IntegerField(default=0)
    ratingDate = models.DateField(auto_now_add=True)
    ratingTime = models.TimeField(auto_now_add=True)
    userCategoryForRating = models.CharField(max_length=100, default='Customer')

    def __str__(self):
        return f"{self.username} : {self.ratingBarCode} : {self.ratingDate}"
    
class ReviewBarcode(models.Model):
    barCode = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.barCode}"
    
class ReviewDelete(models.Model):
    rCode = models.CharField(max_length=100)
    uCode = models.CharField(max_length=100)
    usernames = models.CharField(max_length=500)
    rStar = models.IntegerField(default=1)
    rReview = models.CharField(max_length=5000)
    rDate = models.DateField(auto_now_add=True)
    ratingTime = models.TimeField(auto_now_add=True)
    userCategorySection = models.CharField(max_length=100, default='Customer')

    def __str__(self):
        return f"{self.usernames} : {self.uCode}"
    
class ErrorWork(models.Model):
    lstOfUserVerifationType = [('LOGIN_USER', 'LOGIN_USER'),('NOT_LOGIN_USER', 'NOT_LOGIN_USER')]

    userType = models.CharField(max_length=100, choices=lstOfUserVerifationType, default='NOT_LOGIN_USER')
    uNamesAre = models.CharField(max_length=500, default='NA')
    barCode = models.CharField(max_length=100, default='NOBARCODE1001')
    errorAre = models.CharField(max_length=5000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    urls = models.CharField(max_length=2000, default='NO_URL')

    def __str__(self):
        return f"User Type : {self.userType}, Date & Time : {self.date} {self.time}"