from django.shortcuts import render, HttpResponse, redirect
from taxi_app.models import TaxiAvailable, TaxiBarCode
from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages

# Create your views here.
def HomePageForTaxiAppViewFunction(request):
    return render(request, 'main/home.html')

def reviewPageFunctionBaseView(request):
    return HttpResponse('review page')

# create for coupon code view update, now
def pinTaxiFunctionBaseView(request):
    if request.user.is_authenticated: 
        
        if request.method == 'POST':
            uCityEnter = request.POST.get('uCity'); uCurrentLocationEnter = request.POST.get('uCurrentLocation'); uPincodeEnter = request.POST.get('uPincode'); uTaxiPassengerEnter = abs(int(request.POST.get('uTaxiPassenger')))
            
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
                
                TaxiAvailable(taxiAvaId = newBarCode, taxiCity = uCityEnter, customerId = UDM, currentLocation = uCurrentLocationEnter, pincode = uPincodeEnter, taxiPassenger = uTaxiPassengerEnter).save()
                TaxiBarCode(barCode = newBarCode).save()

                return HttpResponse('SuccessFull Added to Pin Taxi')
            
            else:
                messages.warning(request, 'Passenger Limit is Zero. Then why you need to pin taxi')
                return render(request, 'main/pinTaxi.html')
            
        return render(request, 'main/pinTaxi.html')

    else:
        return redirect('login')