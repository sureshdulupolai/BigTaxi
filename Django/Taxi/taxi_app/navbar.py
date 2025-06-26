from django.contrib.auth.models import User
from Users.models import usersDataModel, ErrorWork
from django.contrib import messages
from taxi_app.models import PinTaxiAvailable
from django.shortcuts import redirect
from datetime import datetime
from Customer.serializers import PinDeleteReviewSerializer, SaveNotificaionDeletePinSerializer

from Customer.models import PinDeleteReview, SaveNotificaionDeletePin

def navbar(request):
    try:
        if request.user.is_authenticated: 
            try:
                checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); 
                userCategoryis = UDM.UserCategory; userBarCodeAccessis = UDM.UserCode; userModelDataCityis = UDM.UserCity; userModelDataStateis = UDM.UserState
                
                city_results = PinTaxiAvailable.objects.filter(taxiCity__icontains=UDM.UserCity)
                if city_results.exists(): results = city_results
                else: results = PinTaxiAvailable.objects.filter(currentLocation__icontains=UDM.UserState)

                for i in results:
                    if i.taxiDateAndTimeByUser == 'none':
                        PDRdata = { "deleteType": "normal", "pinBarCode": i.taxiAvaId, "userBarCode": i.customerId.UserCode, "review": "UnPin Because Of Time Not Mention.", "addressFrom": i.currentLocation, "addressTo": i.toLocation, "date_Time": i.taxiDateAndTimeByUser, "passenger": i.taxiPassenger, "discountCoupon": i.couponCodeWas }
                        SNDPdata = { "barCode": i.taxiAvaId, "userCode": i.customerId.UserCode, "text": f"Your previous taxi was removed because no date/time was mentioned for id : {i.taxiAvaId}" }

                        serializerPDR = PinDeleteReviewSerializer(data = PDRdata)
                        serializerSNDP = SaveNotificaionDeletePinSerializer(data = SNDPdata)

                        if serializerPDR.is_valid() and serializerSNDP.is_valid():
                            serializerPDR.save(); serializerSNDP.save(); i.delete()

                    else:
                        try:
                            if i.driverCode != 'DRIVERCODE':
                                # Extract date + time + AM/PM zone
                                userDateStr = i.taxiDateAndTimeByUser[:10]       # '2025-03-29'
                                userTimeStr = i.taxiDateAndTimeByUser[11:16]     # '04:33'
                                userZoneStr = i.taxiDateAndTimeByUser[16:18]     # 'AM'

                                # Combine to datetime object
                                user_datetime = datetime.strptime(
                                    f"{userDateStr} {userTimeStr} {userZoneStr}", "%Y-%m-%d %I:%M %p"
                                )

                                current_datetime = datetime.now()

                                # ✅ Keep if current <= saved time
                                if (current_datetime > user_datetime) and (int(i.priceOfTravel) == 0):
                                    PDRdata = { "deleteType": "normal", "pinBarCode": i.taxiAvaId, "userBarCode": i.customerId.UserCode, "review": "UnPin Because Time Expired.", "addressFrom": i.currentLocation, "addressTo": i.toLocation, "date_Time": i.taxiDateAndTimeByUser, "passenger": i.taxiPassenger, "discountCoupon": i.couponCodeWas }
                                    SNDPdata = { "barCode": i.taxiAvaId, "userCode": i.customerId.UserCode, "text": f"Your previous taxi was removed because time expired for id : {i.taxiAvaId}" }

                                    serializerPDR = PinDeleteReviewSerializer(data = PDRdata)
                                    serializerSNDP = SaveNotificaionDeletePinSerializer(data = SNDPdata)

                                    if serializerPDR.is_valid() and serializerSNDP.is_valid():
                                        serializerPDR.save(); serializerSNDP.save(); i.delete()
                                
                                elif (current_datetime > user_datetime) and  (int(i.priceOfTravel) != 0): i.runningStatus = 'yes'; i.save()

                        except Exception as e:

                            ErrorWork(userType = 'LOGIN_USER', uNamesAre = request.user.username, barCode = userBarCodeAccessis, errorAre = e, urls = request).save()
                            messages.info(request, 'Oops!, Something Went Wrong in date and time, Please Try Again Later We Will Solve Your Problem Soon!.')
                            return redirect('taxi_app:autoRedirect')
                
                return {'userCategoryis' : userCategoryis, 'userBarCodeAccessis' : userBarCodeAccessis, 'userModelDataCityis' : userModelDataCityis, 'userModelDataStateis' : userModelDataStateis, "profile" : UDM.UProfileImage}
            
            except Exception as e:

                ErrorWork(userType = 'LOGIN_USER', uNamesAre = request.user.username, barCode = userBarCodeAccessis, errorAre = e, urls = request).save()
                messages.info(request, 'Oops!, Something Went Wrong Please Try Again Later We Will Solve Your Problem Soon!.')
                return redirect('taxi_app:autoRedirect')
            
        else:
            return {'userCategoryis' : None, 'userBarCodeAccessis' : None,  'userModelDataCityis' : None, 'userModelDataStateis' : None}

    except Exception as e:
        ErrorWork(userType = 'NOT_LOGIN_USER', errorAre = e, urls = request).save()
        messages.info(request, 'Oops!, Something Went Wrong Please Try Again Later We Will Solve Your Problem Soon!.')
        return redirect('taxi_app:autoRedirect')