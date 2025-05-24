from django.shortcuts import render, HttpResponse, redirect
from taxi_app.models import TaxiBarCode, PinTaxiAvailable
from django.contrib.auth.models import User
from Users.models import usersDataModel, ReviewAndRating, ReviewBarcode
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
import json
from taxi_app.navbar import navbar
from django.urls import reverse

def redirect_based_on_location(request):
    if request.user.is_authenticated:
        context = navbar(request)  # Get city/state
        city = context.get("userModelDataCityis")
        state = context.get("userModelDataStateis")
        
        if city and state:
            return redirect(reverse('taxi_app:home'))
        else:
            return redirect('taxi_app:lan')
    else:
        return redirect('driver:customerLogin')

# Create your views here.
def HomePageForTaxiAppViewFunction(request):
    if request.user.is_authenticated:
        dataFromNavBar = navbar(request)
        city = dataFromNavBar.get("userModelDataCityis")
        state = dataFromNavBar.get("userModelDataStateis")
        userCategory = dataFromNavBar.get('userCategoryis')
        userBarCode = dataFromNavBar.get('userBarCodeAccessis')
        DataOfPinTaxiLst = []

        # if userCategory == 'Driver':
        if request.method == "POST":
            updateCity = request.POST.get('city')
            updateState = request.POST.get('state')
            UDM = usersDataModel.objects.get(UserCode = userBarCode)
            UDM.UserCity = updateCity
            UDM.UserState = updateState
            UDM.save()

            return redirect('taxi_app:home')
        
    else:
        city = request.session.get('userDataCityis', 'defaultCity')
        state = request.session.get('userDataStateis', 'defaultState')

    DataOfPinTaxiLst = PinTaxiAvailable.objects.filter(taxiCity=city)
    if not DataOfPinTaxiLst:
        DataOfPinTaxiLst = PinTaxiAvailable.objects.filter(currentLocation__icontains=state)

    context = {
        'DataOfPinTaxiLst': DataOfPinTaxiLst,
        'city' : city.title(),
        'state' : state.title(),
    }
    return render(request, 'main/home.html', context)


def locationPageFunctionViewBase(request):
    if request.method == "POST":
        city = request.POST.get('uCity'); state = request.POST.get('uState')
        if request.user.is_authenticated:
            uModelData = User.objects.get(username = request.user.username); UDM_Model_Data = usersDataModel.objects.get(ULink = uModelData)
            UDM_Model_Data.UserCity = city; UDM_Model_Data.UserState = state; UDM_Model_Data.save()
        else:
            request.session['userDataCityis'] = city
            request.session['userDataStateis'] = state

        return redirect('taxi_app:home')
    return render(request, 'main/checkLocation.html')

def PointCount(RarLst, values = 1):
    return len([i.userStar for i in RarLst if int(i.userStar) == values])

def reviewPageFunctionBaseView(request):
    if request.user.is_authenticated:
        showData = True; buttonData = []; uNameData = request.user.username
        U = User.objects.get(username = uNameData); data = usersDataModel.objects.get(ULink = U)
        IMG = data.UProfileImage; userName = data.UProfileName

        RarLst = ReviewAndRating.objects.all()
        newRar = [DataInRar for DataInRar in RarLst if str(uNameData) == str(DataInRar.username)]

        if newRar: showData = False; buttonData += [1]; BarCodeOfRating = [DataInNewRar.ratingBarCode for DataInNewRar in newRar][0]
    
        if request.method == 'POST':
            typeOfForm = request.POST.get("formData")

            if typeOfForm == "valueformToNextPage":
                barCode = request.POST.get('')
                pass

            elif typeOfForm == "valueformForSamePage":
                userCodeEnter = request.POST.get('uCode'); userReviewEnter = request.POST.get('uReview'); userStarEnter = int(request.POST.get('uStar')); userCategoryForRatingEnter = request.POST.get('uCategoryForRating'); RBCLst = ReviewBarcode.objects.all(); CodeName = 'REVIEWCODE'; barCodeCreate = ''; 
                
                if len(RBCLst) != 0:
                    RBC = [DataInRBC for DataInRBC in RBCLst]; DataLst = str(RBC[len(RBC) - 1]); newCodes = ''
                    for i in DataLst:
                        if i.isdigit(): newCodes += i
                    barCodeCreate = CodeName + str(int(newCodes) + 1)

                else: noCode = 1064; barCodeCreate = CodeName + str(noCode)

                ReviewAndRating(username = uNameData, userCode = userCodeEnter, ratingBarCode = barCodeCreate, userReview = userReviewEnter or 'Good Service Support', userStar = userStarEnter, userCategoryForRating = str(userCategoryForRatingEnter)).save()
                ReviewBarcode(barCode = barCodeCreate).save()

                return redirect('taxi_app:review')
        
        if len(RarLst) > 0: newRar = newRar + [DataInRar for DataInRar in RarLst if uNameData != DataInRar.username]

        operationUser = []
        for i in newRar:
            uNameCodeSearch = i.userCode; DataIn = usersDataModel.objects.get(UserCode = uNameCodeSearch); operationUser += [(DataIn.UProfileName, DataIn.UProfileImage, i.userStar)]
            buttonData += [0]
        fullReviewLst = zip(newRar, operationUser, buttonData)

        # review count 
        CountData = [i.userStar for i in RarLst]; TotalReview = sum(CountData); TotalCount = len(CountData); 

        if TotalCount != 0: averageStarRating = TotalReview / TotalCount; totalOutOf = round(averageStarRating, 1)
        else: totalOutOf = 0

        countFiveStar = PointCount(RarLst=RarLst, values=5); countFourStar = PointCount(RarLst=RarLst, values=4); countThreeStar = PointCount(RarLst=RarLst, values=3); countTwoStar = PointCount(RarLst=RarLst, values=2); countOneStar = PointCount(RarLst=RarLst, values=1)
        
        if TotalCount != 0: styleFive = countFiveStar / TotalCount * 100; styleFour = countFourStar / TotalCount * 100; styleThree = countThreeStar / TotalCount * 100; styleTwo = countTwoStar / TotalCount * 100; styleOne = countOneStar / TotalCount * 100
        else: styleFive = 0; styleFour = 0; styleThree = 0; styleTwo = 0; styleOne = 0

        context = { 'BarCodeOfRating' : BarCodeOfRating, 'image' : IMG, 'uName' : userName, 'showData' : showData, 'Rar' : fullReviewLst, 'totalOutOf' : totalOutOf, 'countFiveStar' : countFiveStar, 'countFourStar' : countFourStar, 'countThreeStar' : countThreeStar, 'countTwoStar' : countTwoStar, 'countOneStar' : countOneStar, 'styleFive' : styleFive, 'styleFour' : styleFour, 'styleThree' : styleThree, 'styleTwo' : styleTwo, 'styleOne' : styleOne }
        
        return render(request, 'footer/review.html', context)
    
    else:
        showData = False; buttonData = False; RarLst = ReviewAndRating.objects.all(); newRar = [DataInRar for DataInRar in RarLst]; operationUser = []
        for i in newRar:
            uNameCodeSearch = i.userCode; DataIn = usersDataModel.objects.get(UserCode = uNameCodeSearch); operationUser += [(DataIn.UProfileName, DataIn.UProfileImage, i.userStar)]
            buttonData += [0]
        fullReviewLst = zip(newRar, operationUser, buttonData)
        # review count 
        CountData = [i.userStar for i in RarLst]; TotalReview = sum(CountData); TotalCount = len(CountData); 

        if TotalCount != 0: averageStarRating = TotalReview / TotalCount; totalOutOf = round(averageStarRating, 1)
        else: totalOutOf = 0

        countFiveStar = PointCount(RarLst=RarLst, values=5); countFourStar = PointCount(RarLst=RarLst, values=4); countThreeStar = PointCount(RarLst=RarLst, values=3); countTwoStar = PointCount(RarLst=RarLst, values=2); countOneStar = PointCount(RarLst=RarLst, values=1)
        
        if TotalCount != 0: styleFive = countFiveStar / TotalCount * 100; styleFour = countFourStar / TotalCount * 100; styleThree = countThreeStar / TotalCount * 100; styleTwo = countTwoStar / TotalCount * 100; styleOne = countOneStar / TotalCount * 100
        else: styleFive = 0; styleFour = 0; styleThree = 0; styleTwo = 0; styleOne = 0
        
        messages.info(request, 'To post a review in BigTaxi. Login, Now!')
        context = { 'showData' : showData, 'Rar' : fullReviewLst, 'totalOutOf' : totalOutOf, 'countFiveStar' : countFiveStar, 'countFourStar' : countFourStar, 'countThreeStar' : countThreeStar, 'countTwoStar' : countTwoStar, 'countOneStar' : countOneStar, 'styleFive' : styleFive, 'styleFour' : styleFour, 'styleThree' : styleThree, 'styleTwo' : styleTwo, 'styleOne' : styleOne }
        return render(request, 'footer/review.html', context)
    
def deleteReviewFunctionBaseView(request):
    pass


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