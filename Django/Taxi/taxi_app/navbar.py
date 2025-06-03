from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages
from taxi_app.models import PinTaxiAvailable
from Customer.models import PinDeleteReview, SaveNotificaionDeletePin
from django.shortcuts import render
from datetime import datetime

def navbar(request):
    if request.user.is_authenticated: 
        
        checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); 
        userCategoryis = UDM.UserCategory; userBarCodeAccessis = UDM.UserCode; userModelDataCityis = UDM.UserCity; userModelDataStateis = UDM.UserState

        city_results = PinTaxiAvailable.objects.filter(taxiCity__icontains=UDM.UserCity)
        if city_results.exists(): results = city_results
        else: results = PinTaxiAvailable.objects.filter(currentLocation__icontains=UDM.UserState)

        for i in results:
            userDate = i.taxiDateAndTimeByUser[:10]
            userTime = i.taxiDateAndTimeByUser[11:16]
            userZone = i.taxiDateAndTimeByUser[16:18]

            now = datetime.now()
            current_date = str(now.strftime("%Y-%m-%d"))
            currentDate = str(now.strftime("%I:%M:%S %p"))
            current_Time, current_Zone = currentDate[:5], currentDate[9:11]
            
            if i.taxiDateAndTimeByUser == 'none':
                
                PinDeleteReview(deleteType = 'normal', pinBarCode= i.taxiAvaId, userBarCode = i.customerId.UserCode, review = 'UnPin Because Of Time Not Mention.', addressFrom = i.currentLocation, addressTo = i.toLocation, date_Time = i.taxiDateAndTimeByUser, passenger = i.taxiPassenger, discountCoupon = i.couponCodeWas).save()
                SaveNotificaionDeletePin(barCode = i.taxiAvaId, userCode = i.customerId.UserCode, text = f"Your previous taxi was removed because no date/time was mentioned for id : {i.taxiAvaId}").save()
                i.delete()

        return {'userCategoryis' : userCategoryis, 'userBarCodeAccessis' : userBarCodeAccessis, 'userModelDataCityis' : userModelDataCityis, 'userModelDataStateis' : userModelDataStateis}
    
    else:
        return {'userCategoryis' : None, 'userBarCodeAccessis' : None,  'userModelDataCityis' : None, 'userModelDataStateis' : None}