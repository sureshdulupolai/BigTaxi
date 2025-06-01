from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages
from taxi_app.models import PinTaxiAvailable
from Customer.models import PinDeleteReview, SaveNotificaionDeletePin
from django.shortcuts import render

def navbar(request):
    if request.user.is_authenticated: 
        
        checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); 
        userCategoryis = UDM.UserCategory; userBarCodeAccessis = UDM.UserCode; userModelDataCityis = UDM.UserCity; userModelDataStateis = UDM.UserState

        city_results = PinTaxiAvailable.objects.filter(taxiCity__icontains=UDM.UserCity)
        if city_results.exists(): results = city_results
        else: results = PinTaxiAvailable.objects.filter(currentLocation__icontains=UDM.UserState)

        for i in results:
            if i.taxiDateAndTimeByUser == 'none':
                
                PinDeleteReview(deleteType = 'normal', pinBarCode= i.taxiAvaId, userBarCode = i.customerId.UserCode, review = 'UnPin Because Of Time Not Mention.', addressFrom = i.currentLocation, addressTo = i.toLocation, date_Time = i.taxiDateAndTimeByUser, passenger = i.taxiPassenger, discountCoupon = i.couponCodeWas).save()
                SaveNotificaionDeletePin(barCode = i.taxiAvaId, userCode = i.customerId.UserCode, text = f"Your previous taxi was removed because no date/time was mentioned for id : {i.taxiAvaId}").save()
                i.delete()

        return {'userCategoryis' : userCategoryis, 'userBarCodeAccessis' : userBarCodeAccessis, 'userModelDataCityis' : userModelDataCityis, 'userModelDataStateis' : userModelDataStateis}
    
    else:
        return {'userCategoryis' : None, 'userBarCodeAccessis' : None,  'userModelDataCityis' : None, 'userModelDataStateis' : None}