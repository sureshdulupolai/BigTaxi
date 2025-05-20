from django.shortcuts import render, HttpResponse, redirect
from taxi_app.models import TaxiBarCode, PinTaxiAvailable
from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages

# Create your views here.
def HomePageForTaxiAppViewFunction(request):
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
                uCityEnter = request.POST.get('uCity'); uCurrentLocationEnter = request.POST.get('uCurrentLocation'); uPincodeEnter = request.POST.get('uPincode'); uTaxiPassengerEnter = abs(int(request.POST.get('uTaxiPassenger'))); uCouponCodeEnter = request.POST.get('uCouponCode'); uVerifyStatusEnter = request.POST.get('uVerifyStatus'); uBarCodeEnter = request.POST.get('uBarCode'); uLastLocationEnter = request.POST.get('uLastLocation')
                if uVerifyStatusEnter == "Driver":
                    uCouponCode = usersDataModel.objects.get(UserCode = uBarCodeEnter)
                    uCouponCodeEnter = uCouponCode.CouponCode

                else:
                    if uCouponCodeEnter: pass
                    else: uCouponCodeEnter = 'Customer Not Have Coupon'

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
                    
                    PinTaxiAvailable(taxiAvaId = newBarCode, taxiCity = uCityEnter, customerId = UDM, currentLocation = uCurrentLocationEnter, pincode = uPincodeEnter, taxiPassenger = uTaxiPassengerEnter, couponCodeWas = uCouponCodeEnter, toLocation = uLastLocationEnter).save()
                    TaxiBarCode(barCode = newBarCode).save()

                    return HttpResponse('SuccessFull Added to Pin Taxi')
                
                else:
                    messages.warning(request, 'Passenger Limit is Zero. Then why you need to pin taxi')
                    return render(request, 'main/pinTaxi.html')
        
        else:
            DataShow = False
            
        context = {'valueOfPin' : valueOfPin, 'dataOfPin' : dataOfPin, 'usernames' : usernames, 'DataShow' : DataShow, 'profileImage' : profileImage}
        return render(request, 'main/pinTaxi.html', context)

    else:
        return redirect('driver:login')