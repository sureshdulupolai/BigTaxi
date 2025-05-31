from django.shortcuts import render, HttpResponse, redirect
from taxi_app.models import TaxiBarCode, PinTaxiAvailable
from django.contrib.auth.models import User
from Users.models import usersDataModel, ReviewAndRating, ReviewBarcode, ReviewDelete
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
import json
from taxi_app.navbar import navbar
from django.urls import reverse
from Driver.models import DriverAcceptedPin, ReportDriverInPinTaxi
from Customer.models import PinDeleteReview

def redirect_based_on_location(request):
    if request.user.is_authenticated:
        context = navbar(request); city = context.get("userModelDataCityis"); state = context.get("userModelDataStateis")
        if city and state: return redirect(reverse('taxi_app:home'))
        else: return redirect('taxi_app:lan')
    else: return redirect('driver:customerLogin')

# Create your views here.
def HomePageForTaxiAppViewFunction(request):
    DataOfPinTaxiLst = []; newLstOfDPTL = []; showError = [1, 1, 1]

    if request.user.is_authenticated:
        dataFromNavBar = navbar(request)
        city = dataFromNavBar.get("userModelDataCityis"); state = dataFromNavBar.get("userModelDataStateis"); userCategory = dataFromNavBar.get('userCategoryis'); userBarCode = dataFromNavBar.get('userBarCodeAccessis')
        
        # if userCategory == 'Driver':
        if request.method == "POST":
            checkFormProcess = request.POST.get('checkForm')

            if checkFormProcess == 'FormOneSelectByUser':
                updateCity = request.POST.get('city'); updateState = request.POST.get('state'); UDM = usersDataModel.objects.get(UserCode = userBarCode); UDM.UserCity = updateCity; UDM.UserState = updateState
                UDM.save()
                return redirect('taxi_app:home')
            
            elif checkFormProcess == 'FormTwoSelectByUser':
                BarCodeDetails = request.POST.get('userPinCode')
                request.session['userPinDetailsCodeTaxi'] = BarCodeDetails
                return redirect('taxi_app:pinDetail', barCode= BarCodeDetails)
        
    else: city = request.session.get('userDataCityis', 'defaultCity'); state = request.session.get('userDataStateis', 'defaultState')

    DataOfPinTaxiLst = PinTaxiAvailable.objects.filter(taxiCity=city)
    if not DataOfPinTaxiLst: DataOfPinTaxiLst = PinTaxiAvailable.objects.filter(currentLocation__icontains=state)

    if DataOfPinTaxiLst: 
        showError = [1 if ReportDriverInPinTaxi.objects.filter(pinBarCode=PinTaxiAvailable.objects.get(taxiAvaId=i.taxiAvaId)).last() else 0 for i in DataOfPinTaxiLst]
        newLstOfDPTL = [(i.customerId.UProfileImage, i.customerId.UProfileName or 'BigTaxi Customer') for i in DataOfPinTaxiLst] if DataOfPinTaxiLst else []

    newDataOfBoth = zip(DataOfPinTaxiLst, newLstOfDPTL, showError)

    context = { 'DataOfPinTaxiLst': newDataOfBoth, 'city' : city.title(), 'state' : state.title() }
    return render(request, 'main/home.html', context)

def pinDetailFunctionBaseView(request,barCode):
    pinCodeHere = request.session.get('userPinDetailsCodeTaxi' or False); userTravelFrom = ''; userTravelTo = ''; passenger = 1; dateAndTime = ''; customerImage = ''; customerName = '';  customerUsername = ''; verifyUser = 'UnTrusted'; gender = 'Male'; dataShow = True
    ShowPriceDataInTemplate = True; PriceExist = 0
    if pinCodeHere:
        if barCode == pinCodeHere:

            if request.method == 'POST':
                travelPrice = int(request.POST.get('price')); PTA = PinTaxiAvailable.objects.get(taxiAvaId = pinCodeHere)
                if int(PTA.priceOfTravel) > int(travelPrice): userCodeBar = usersDataModel.objects.get(ULink = User.objects.get(username = request.user.username)).UserCode; PTA.driverCode = userCodeBar; PTA.priceOfTravel = travelPrice; PTA.save(); DriverAcceptedPin(priceAccepted = travelPrice,pinBarCode = pinCodeHere,userCode = userCodeBar).save()
# redirect to accepted page remaning
                else: messages.info(request, f'another user have choosed : {PinTaxiAvailable.objects.get(taxiAvaId = pinCodeHere).priceOfTravel}₹'); return redirect('taxi_app:pinDetail', barCode=pinCodeHere)

            DAP = DriverAcceptedPin.objects.all()
            for DataInDAP in DAP:
                navData = navbar(request)
                if DataInDAP.userCode == navData['userBarCodeAccessis'] and DataInDAP.pinBarCode == pinCodeHere:
                    ShowPriceDataInTemplate = False
                    PriceExist = DataInDAP.priceAccepted
            
            DataOfPinUser = PinTaxiAvailable.objects.get(taxiAvaId = pinCodeHere); userTravelFrom = DataOfPinUser.currentLocation; userTravelTo = DataOfPinUser.toLocation; dateAndTime = DataOfPinUser.taxiDateAndTimeByUser; customerImage = DataOfPinUser.customerId.UProfileImage; customerName = DataOfPinUser.customerId.UProfileName.title(); customerUsername = DataOfPinUser.customerId.ULink.username; gender = DataOfPinUser.customerId.UserGender.title(); DangerTripCount = int(DataOfPinUser.customerId.dangerTripCount)
            if gender == 'Not Check': dataShow = False

            if DangerTripCount == 0: verifyUser = 'Trusted'
            elif DangerTripCount >= 0 and DangerTripCount <= 5: verifyUser = 'SomeTrust'
            elif DangerTripCount >= 6: verifyUser = 'NoTrust'

        else:
            messages.warning(request ,"don't change any id of taxi details")
            return redirect('taxi_app:autoRedirect')
            
    else:
        messages.warning(request, "can't reach this page for now!")
        return redirect('taxi_app:autoRedirect')
    
    context = { 'barCode' : barCode, 'PriceExist' : PriceExist, 'ShowPriceDataInTemplate' : ShowPriceDataInTemplate, 'userTravelFrom' : userTravelFrom, 'userTravelTo' : userTravelTo, 'passenger' : passenger, 'dateAndTime' : dateAndTime, 'customerImage' : customerImage, 'customerName' : customerName, 'customerUsername' : customerUsername, 'verifyUser' : verifyUser, 'gender' : gender, 'dataShow' : dataShow }
    return render(request, 'main/details.html', context)

def reportDriverOnPinTaxiFunctionBaseView(request, barCodes):
    PinData = request.session.get('userPinDetailsCodeTaxi' or False); navData = navbar(request)

    if PinData:

        if PinData == barCodes:

            if request.method == 'POST':
                
                reportDataEnter = request.POST.get('reportData'); reportForEnter = request.POST.get('reportFor')
                ReportDriverInPinTaxi(pinBarCode = PinTaxiAvailable.objects.get(taxiAvaId = PinData), driverCode = navData['userBarCodeAccessis'], driverReportFor = reportForEnter, reportData = reportDataEnter).save()
                messages.success(request, f'successfully, reported done for Id : {barCodes}')
        
        else:
            messages.warning(request ,"don't change any id of taxi report page, while reporting.")
            return redirect('taxi_app:pinDetail', barCode = PinData)
        
    else:
        messages.warning(request, "can't reach this page for now!")
        return redirect('taxi_app:autoRedirect')
    
    context = {'barCodeHere' : barCodes}
    return render(request, 'main/reportPin.html', context)

def locationPageFunctionViewBase(request):
    if request.method == "POST":
        city = request.POST.get('uCity'); state = request.POST.get('uState')
        if request.user.is_authenticated: uModelData = User.objects.get(username = request.user.username); UDM_Model_Data = usersDataModel.objects.get(ULink = uModelData); UDM_Model_Data.UserCity = city; UDM_Model_Data.UserState = state; UDM_Model_Data.save()
        else: request.session['userDataCityis'] = city; request.session['userDataStateis'] = state
        return redirect('taxi_app:home')
    
    return render(request, 'main/checkLocation.html')

def PointCount(RarLst, values = 1):
    return len([i.userStar for i in RarLst if int(i.userStar) == values])

def reviewPageFunctionBaseView(request):
    showData = False; buttonData = []; RarLst = ReviewAndRating.objects.all(); operationUser = []
    if request.user.is_authenticated:
        uNameData = request.user.username; BarCodeOfRating = []; newRar = [DataInRar for DataInRar in RarLst if str(uNameData) == str(DataInRar.username)]
        # U = User.objects.get(username = uNameData); data = usersDataModel.objects.get(ULink = U)
        if newRar: showData = False; buttonData += [1]; BarCodeOfRating = [DataInNewRar.ratingBarCode for DataInNewRar in newRar][0]
    
        if request.method == 'POST':
            typeOfForm = request.POST.get("formData")

            if typeOfForm == "formToNextPage":
                barCode = request.POST.get('dataInHid'); request.session['userRatingCode'] = barCode
                return redirect('taxi_app:deleteReview')

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

        for i in newRar: 
            uNameCodeSearch = i.userCode; DataIn = usersDataModel.objects.get(UserCode = uNameCodeSearch); operationUser += [(DataIn.UProfileName, DataIn.UProfileImage, i.userStar)]; buttonData += [0]
        fullReviewLst = zip(newRar, operationUser, buttonData)

        # review count 
        CountData = [i.userStar for i in RarLst]; TotalReview = sum(CountData); TotalCount = len(CountData); 

        if TotalCount != 0: averageStarRating = TotalReview / TotalCount; totalOutOf = round(averageStarRating, 1)
        else: totalOutOf = 0

        countFiveStar = PointCount(RarLst=RarLst, values=5); countFourStar = PointCount(RarLst=RarLst, values=4); countThreeStar = PointCount(RarLst=RarLst, values=3); countTwoStar = PointCount(RarLst=RarLst, values=2); countOneStar = PointCount(RarLst=RarLst, values=1)
        
        if TotalCount != 0: styleFive = countFiveStar / TotalCount * 100; styleFour = countFourStar / TotalCount * 100; styleThree = countThreeStar / TotalCount * 100; styleTwo = countTwoStar / TotalCount * 100; styleOne = countOneStar / TotalCount * 100
        else: styleFive = 0; styleFour = 0; styleThree = 0; styleTwo = 0; styleOne = 0

        context = { 'BarCodeOfRating' : BarCodeOfRating, 'showData' : showData, 'Rar' : fullReviewLst, 'totalOutOf' : totalOutOf, 'countFiveStar' : countFiveStar, 'countFourStar' : countFourStar, 'countThreeStar' : countThreeStar, 'countTwoStar' : countTwoStar, 'countOneStar' : countOneStar, 'styleFive' : styleFive, 'styleFour' : styleFour, 'styleThree' : styleThree, 'styleTwo' : styleTwo, 'styleOne' : styleOne }
        
        return render(request, 'footer/review.html', context)
    
    else:
        newRar = [DataInRar for DataInRar in RarLst]
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
    if request.user.is_authenticated:
        DataInBar = request.session.get('userRatingCode', False)

        if DataInBar:

            if request.method == "POST":

                try:
                    RR = ReviewAndRating.objects.get(ratingBarCode = DataInBar); ReviewDelete(usernames = request.user.username, rCode = RR.ratingBarCode, uCode = RR.userCode, rStar = RR.userStar, rReview = RR.userReview, userCategorySection = RR.userCategoryForRating).save(); RR.delete()
                    return redirect('taxi_app:review')
                
                except:
                    messages.warning(request, "You can't delete a review. you don't have access to delete")
                    return render(request, 'more/pageNotFound.html')
                
            return render(request, 'footer/deleteReview.html')
        
        else:
            messages.warning(request, "You can't reach this page for now.")
            return render(request, 'more/pageNotFound.html')
        
    else:
        return redirect('driver:customerLogin')

def PinFunction(request, dataPresentLst):
    dataOfPinLst = []; IdLst = []; codeLst = []
    for a1 in dataPresentLst:
        dataOfPinLst += [a1]
    DataOf = [1 if ReportDriverInPinTaxi.objects.filter(pinBarCode = i) else 0 for i in dataPresentLst]

    if 1 in DataOf:
        indexPosition, NoIndex = [index for index, value in enumerate(DataOf) if value == 1], [index for index, value in enumerate(DataOf) if value == 0]
        for i in indexPosition: IdLst.append(str(dataOfPinLst[i].taxiAvaId)); codeLst.append(str(dataOfPinLst[i].taxiAvaId))
        for j in NoIndex: IdLst.insert(j, '')

    request.session['ReportAccessBarCode'] = codeLst
    DataZip = list(zip(dataOfPinLst, DataOf))
    return DataZip

# create for coupon code view update, now
def pinTaxiFunctionBaseView(request):
    if request.user.is_authenticated: 
        showMessage = False
        usernames = request.user.username; user = User.objects.get(username = usernames); dataOfUser = usersDataModel.objects.get(ULink = user); dataPresentLst = PinTaxiAvailable.objects.filter(customerId = dataOfUser)
        # default form limit is 2
        profileImage = dataOfUser.UProfileImage; setLimitToForm = 2

        if dataPresentLst:
            valueOfPin = True

            if len(dataPresentLst) > 1:dataOfPin = PinFunction(request, dataPresentLst)
            elif len(dataPresentLst) > 3: dataOfPin = PinFunction(request, dataPresentLst)
            else:  dataOfPin = PinFunction(request, dataPresentLst)

        else: valueOfPin = False; dataOfPin = False

        if len(dataPresentLst) < setLimitToForm:
            DataShow = True
            
            if request.method == 'POST':
                uCityEnter = request.POST.get('uCity'); uCurrentLocationEnter = request.POST.get('uCurrentLocation'); uPincodeEnter = request.POST.get('uPincode'); uTaxiPassengerEnter = abs(int(request.POST.get('uTaxiPassenger'))); uCouponCodeEnter = request.POST.get('uCouponCode'); uVerifyStatusEnter = request.POST.get('uVerifyStatus'); uBarCodeEnter = request.POST.get('uBarCode'); uLastLocationEnter = request.POST.get('uLastLocation'); utaxiDateAndTimeByUserEnter = request.POST.get('utaxiDateAndTimeByUser')
                # driver default coupon code
                if uVerifyStatusEnter == "Driver": uCouponCode = usersDataModel.objects.get(UserCode = uBarCodeEnter); uCouponCodeEnter = uCouponCode.CouponCode

                else:
                    if uCouponCodeEnter: pass
                    else: uCouponCodeEnter = 'Customer Not Have Coupon'

                # Convert to desired format: "2025-05-29 11:30AM"
                if utaxiDateAndTimeByUserEnter: dt_obj = datetime.strptime(utaxiDateAndTimeByUserEnter, "%Y-%m-%dT%H:%M"); formatted_datetime = dt_obj.strftime("%Y-%m-%d %I:%M%p")  # %I = 12-hour, %p = AM/PM
                else: formatted_datetime = "none"

                if uTaxiPassengerEnter > 0:
                    checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); CodeNameTaxiAva = 'TAXIAVALIABLE'; CodeNo = 101; TBC = TaxiBarCode.objects.all()
                    
                    if len(TBC) > 0:
                        barLst = [TBCData.barCode for TBCData in TBC]; oldBarCode = barLst[len(barLst) - 1]; newCodes = ''
                        for i in oldBarCode:
                            if i.isdigit(): newCodes += i
                        newBarCode = CodeNameTaxiAva + str(int(newCodes) + 1)

                    else: newBarCode = CodeNameTaxiAva + str(CodeNo)
                    
                    PinTaxiAvailable(taxiAvaId = newBarCode, taxiCity = uCityEnter, customerId = UDM, currentLocation = uCurrentLocationEnter, pincode = uPincodeEnter, taxiPassenger = uTaxiPassengerEnter, couponCodeWas = uCouponCodeEnter, toLocation = uLastLocationEnter, taxiDateAndTimeByUser = formatted_datetime).save(); TaxiBarCode(barCode = newBarCode).save()
                    return redirect('taxi_app:pinTaxi')
                
                else: messages.warning(request, 'Passenger Limit is Zero. Then why you need to pin taxi'); showMessage = True; return render(request, 'main/pinTaxi.html')
        
        else: DataShow = False
        
        context = { 'showMessage' : showMessage, 'valueOfPin' : valueOfPin, 'dataOfPin' : dataOfPin, 'usernames' : usernames, 'DataShow' : DataShow, 'profileImage' : profileImage}
        return render(request, 'main/pinTaxi.html', context)

    else: return redirect('driver:login')

def checkPinTaxiReportFunctionBaseView(request, barCodeId):
    Codelst = request.session.get('ReportAccessBarCode' or False)
    usernames = ''; report = ''; date_time = ''
    if Codelst:
        if barCodeId in Codelst:
            PTA = PinTaxiAvailable.objects.get(taxiAvaId = barCodeId)
            RDPT = ReportDriverInPinTaxi.objects.get(pinBarCode = PTA)
            usernames = usersDataModel.objects.get(UserCode = RDPT.driverCode).ULink.username
            report = RDPT.reportData
            date_time = str(RDPT.date) + ' ' + str(RDPT.time)

        else:
            messages.warning(request, "Don't change anybarcode while accessing report")
            return redirect('taxi_app:pinTaxi')
    else:
        messages.warning(request, 'Currently Cant Reach this page')
        return redirect('taxi_app:pinTaxi')
    
    context = { 'usernames' : usernames, 'report' : report, 'date_time' : date_time }
    return render(request, 'main/checkReport.html', context)

def deletePinTaxiReport(request, codeNeed):
    referrer = request.META.get('HTTP_REFERER')
    if referrer:
        PTA_Object = PinTaxiAvailable.objects.get(taxiAvaId = codeNeed)
        ReviewObject = ReportDriverInPinTaxi.objects.get(pinBarCode = PTA_Object)

        try:
            if request.method == 'POST':
            
                PinDeleteReview(
                        deleteType = 'report',
                        pinBarCode = PTA_Object.taxiAvaId,
                        userBarCode = PTA_Object.customerId.UserCode,
                        driverCode = PTA_Object.driverCode,
                        addressFrom = PTA_Object.currentLocation,
                        addressTo = PTA_Object.toLocation,
                        date_Time = str(PTA_Object.taxiDate) + ' ' + str(PTA_Object.taxiTime),
                        passenger = str(PTA_Object.taxiPassenger),
                        review = ReviewObject.reportData,
                        price = str(PTA_Object.priceOfTravel),
                        discountCoupon = PTA_Object.couponCodeWas
                ).save()

                PTA_Object.delete(); ReviewObject.delete()

                messages.success(request, f'Pin Taxi Report Details Is Deleted SuccessFully, For Id {codeNeed}')
                return redirect('taxi_app:pinTaxi')


        except:
            messages.info(request, 'page not found, or Something Got Miss Matched Try Again!')
            return redirect('taxi_app:pinTaxi')
        
    else:
        # User didn't type manually — show 404
        messages.success(request, "Can't getting the page!, please click on delete button to access that page, data will fetch automatic.")
        return redirect('taxi_app:pinTaxi')
    
    context = {'CodeId' : codeNeed}
    return render(request, 'main/deletetRepost.html', context)

def deletePinTaxiDetailsNoReport(request, codeNeed):
    referrer = request.META.get('HTTP_REFERER')

    if referrer:
        PTA_Object = PinTaxiAvailable.objects.get(taxiAvaId = codeNeed)

        if request.method == 'POST':
            
            try:
                PinDeleteReview(
                    deleteType = 'normal',
                    pinBarCode = PTA_Object.taxiAvaId,
                    userBarCode = PTA_Object.customerId.UserCode,
                    driverCode = PTA_Object.driverCode,
                    addressFrom = PTA_Object.currentLocation,
                    addressTo = PTA_Object.toLocation,
                    date_Time = str(PTA_Object.taxiDate) + ' ' + str(PTA_Object.taxiTime),
                    passenger = str(PTA_Object.taxiPassenger),
                    price = str(PTA_Object.priceOfTravel),
                    discountCoupon = PTA_Object.couponCodeWas,
                    review = request.POST.get('report')
                ).save()

                PTA_Object.delete()

                messages.success(request, f'Pin Taxi Details Is Deleted SuccessFully, For Id {codeNeed}')
                return redirect('taxi_app:pinTaxi')
            
            except Exception as e:
                print('Error -  ', e)
                messages.info(request, 'page not found, or Something Got Miss Matched Try Again!')
                return redirect('taxi_app:pinTaxi')

    else:
        # User didn't type manually — show 404
        messages.success(request, "Can't getting the page!, please click on delete button to access that page, data will fetch automatic.")
        return redirect('taxi_app:pinTaxi')
    
    context = {'CodeId' : codeNeed}
    return render(request, 'main/deleteDetailsPin.html', context)

def checkStatusOfPinFunctionBaseView(request, IdCodeNeed):
    IdCodeNeed = IdCodeNeed.upper()
    localTime = ''; showMoreDetailsInTemplete = False; price = ''

    try:
        PTA_LstOfObject = PinTaxiAvailable.objects.get(taxiAvaId = IdCodeNeed)
        RDPTObject = ReportDriverInPinTaxi.objects.filter(pinBarCode = PTA_LstOfObject)
        
    except Exception as e:
        if str(e) == 'PinTaxiAvailable matching query does not exist.':
            messages.info(request, f"Need a Proper Id, This id is does'nt exist {IdCodeNeed}.")
            return redirect('taxi_app:pinTaxi')
        else:
            messages.info(request, "Can't reach this page for not try again after sometime.")
            return redirect('taxi_app:pinTaxi')
        
    if not RDPTObject:

        if int(str(PTA_LstOfObject.taxiTime)[:2]) < 12: localTime = 'am'
        else: localTime = 'pm'

        if PTA_LstOfObject.driverCode != 'DRIVERCODE':  driverData = usersDataModel.objects.get(UserCode = PTA_LstOfObject.driverCode).UProfileName; showMoreDetailsInTemplete = True; price = PTA_LstOfObject.priceOfTravel
        else: driverData = 'Driver Not Assigned'

    else:
        messages.info(request, f"Can't show status for this ID {IdCodeNeed}, Detail in reported for now.")
        return redirect('taxi_app:pinTaxi')

    context = { 'userName' : PTA_LstOfObject.customerId.UProfileName, 'statusCode' : PTA_LstOfObject.taxiAvaId, 'stLocation' : PTA_LstOfObject.currentLocation, 'lsLoction' : PTA_LstOfObject.toLocation, 'dateAndTime' : str(PTA_LstOfObject.taxiDate) + '  ' + str(PTA_LstOfObject.taxiTime)[:5] + ' ' + localTime, 'passenger' : PTA_LstOfObject.taxiPassenger, 'ShowMore' : showMoreDetailsInTemplete, 'DriverName' : driverData, 'price' : price }
    return render(request, 'main/checkStatus.html', context)
