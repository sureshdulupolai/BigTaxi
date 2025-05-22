from django.shortcuts import render, HttpResponse, redirect
from taxi_app.models import TaxiBarCode, PinTaxiAvailable
from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
import json


# Create your views here.
def HomePageForTaxiAppViewFunction(request):
    if request.method == "POST" and request.user.is_authenticated:
        try:
            
            data = json.loads(request.body)
            userBarCode = data.get('barcode')
            userCategory = data.get('category')
            userStateByWindow = data.get('state')

            print(userStateByWindow, 'Current State')
            if (userCategory != None) and userBarCode:
                print('Code Access In Python')
                userCurrentCity = usersDataModel.objects.get(UserCode = userBarCode).UserCity
                if (userCurrentCity == '') and (userStateByWindow != ''):
                    userCurrentCity = userStateByWindow

            if userCategory == 'Driver':
                print('Driver')
                DataOfPinTaxiLst = PinTaxiAvailable.objects.filter(taxiCity = 1)
                for DPTL in DataOfPinTaxiLst:
                    print(DPTL.currentLocation)

            elif userCategory == 'Customer':
                pass
            elif userCategory == 'Developer':
                pass
            else:
                pass


        except json.JSONDecodeError:
            print("Invalid JSON received")

        return JsonResponse({'status': 'received'})

    # If GET, just render the page
    return render(request, 'main/home.html')

def reviewPageFunctionBaseView(request):
    if request.user.is_authenticated: 
        return HttpResponse('review page')
    else:
        return redirect('driver:login')

def PinFunction(dataPresentLst):
    dataOfPinLst = []
    for a1 in dataPresentLst:
        dataOfPinLst += [a1]
    return dataOfPinLst
    
# create for coupon code view update, now
def pinTaxiFunctionBaseView(request):
    if request.user.is_authenticated: 
        usernames = request.user.username; user = User.objects.get(username = usernames); dataOfUser = usersDataModel.objects.get(ULink = user); dataPresentLst = PinTaxiAvailable.objects.filter(customerId = dataOfUser)
        # default form limit is 2
        profileImage = dataOfUser.UProfileImage; setLimitToForm = 4

        if dataPresentLst:
            valueOfPin = True
            if len(dataPresentLst) > 1:
                # ask, one is already added you need to add more ?
                dataOfPin = PinFunction(dataPresentLst)

            elif len(dataPresentLst) > 3:
                # not allowed, already three added
                dataOfPin = PinFunction(dataPresentLst)
            else: 
                dataOfPin = PinFunction(dataPresentLst)

        else: valueOfPin = False; dataOfPin = False

        if len(dataPresentLst) < setLimitToForm:
            DataShow = True
            # post method
            if request.method == 'POST':
                uCityEnter = request.POST.get('uCity'); uCurrentLocationEnter = request.POST.get('uCurrentLocation'); uPincodeEnter = request.POST.get('uPincode'); uTaxiPassengerEnter = abs(int(request.POST.get('uTaxiPassenger'))); uCouponCodeEnter = request.POST.get('uCouponCode'); uVerifyStatusEnter = request.POST.get('uVerifyStatus'); uBarCodeEnter = request.POST.get('uBarCode'); uLastLocationEnter = request.POST.get('uLastLocation'); utaxiDateAndTimeByUserEnter = request.POST.get('utaxiDateAndTimeByUser')
                if uVerifyStatusEnter == "Driver":
                    uCouponCode = usersDataModel.objects.get(UserCode = uBarCodeEnter)
                    uCouponCodeEnter = uCouponCode.CouponCode

                else:
                    if uCouponCodeEnter: pass
                    else: uCouponCodeEnter = 'Customer Not Have Coupon'

                # Convert to desired format: "2025-05-29 11:30AM"
                if utaxiDateAndTimeByUserEnter:
                    dt_obj = datetime.strptime(utaxiDateAndTimeByUserEnter, "%Y-%m-%dT%H:%M")
                    formatted_datetime = dt_obj.strftime("%Y-%m-%d %I:%M%p")  # %I = 12-hour, %p = AM/PM
                else:
                    formatted_datetime = "none"

                if uTaxiPassengerEnter > 0:
                    checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); 
                    CodeNameTaxiAva = 'TAXIAVALIABLE'; CodeNo = 101; TBC = TaxiBarCode.objects.all()
                    
                    if len(TBC) > 0:
                        barLst = [TBCData.barCode for TBCData in TBC]; oldBarCode = barLst[len(barLst) - 1]; newCodes = ''
                        for i in oldBarCode:
                            if i.isdigit(): newCodes += i
                        newBarCode = CodeNameTaxiAva + str(int(newCodes) + 1)

                    else:
                        newBarCode = CodeNameTaxiAva + str(CodeNo)
                    
                    PinTaxiAvailable(taxiAvaId = newBarCode, taxiCity = uCityEnter, customerId = UDM, currentLocation = uCurrentLocationEnter, pincode = uPincodeEnter, taxiPassenger = uTaxiPassengerEnter, couponCodeWas = uCouponCodeEnter, toLocation = uLastLocationEnter, taxiDateAndTimeByUser = formatted_datetime).save()
                    TaxiBarCode(barCode = newBarCode).save()

                    return redirect('taxi_app:pinTaxi')
                
                else:
                    messages.warning(request, 'Passenger Limit is Zero. Then why you need to pin taxi')
                    return render(request, 'main/pinTaxi.html')
        
        else:
            DataShow = False
            
        context = {'valueOfPin' : valueOfPin, 'dataOfPin' : dataOfPin, 'usernames' : usernames, 'DataShow' : DataShow, 'profileImage' : profileImage}
        return render(request, 'main/pinTaxi.html', context)

    else:
        return redirect('driver:login')