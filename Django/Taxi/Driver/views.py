from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Driver.models import driverDataModel, DriverModelStore
from Users.models import usersDataModel
from django.contrib.auth import login
from django.contrib.auth import logout

# login
def driverLoginFunctionBaseView(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already login into BigTaxi, Driver Department '{}'".format(request.user.username))
        return redirect('taxi_app:home')
    
    else:
        if request.method == 'POST':
            userMobileNo = int(request.POST.get('mobileNo')); userPass = request.POST.get('password1')

            strMobileNo = str(userMobileNo)
            if userMobileNo and userPass and (len(strMobileNo) == 10):

                try:
                    user_data = usersDataModel.objects.get(
                        UserCategory='Driver',
                        UserMobileNo=strMobileNo,
                        UserPass=userPass
                    )
                    
                    # Django login
                    login(request, user_data.ULink)  # user_data.ULink is actual Django User model
                    newOfUser = user_data.ULink.username
                
                    # Store category also in session (for navbar)
                    request.session['userCategoryis'] = user_data.UserCategory
                    messages.success(request, 'Successfully login into BigTaxi {}'.format(newOfUser))
                    return redirect('taxi_app:home')
                
                except usersDataModel.DoesNotExist:
                    messages.warning(request, 'Invalid Mobile Number or Password.')
            else:
                messages.warning(request, 'Enter a valid 10-digit mobile number.')

        return render(request, 'login/driverLogin.html')

def customerLoginFunctionBaseView(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already login into BigTaxi, Customer Department '{}'".format(request.user.username))
        return redirect('taxi_app:home')

    else:
        if request.method == 'POST':
            userMobileNo = int(request.POST.get('mobileNo')); userPass = request.POST.get('password1')

            strMobileNo = str(userMobileNo)
            if userMobileNo and userPass and (len(strMobileNo) == 10):

                try:
                    user_data = usersDataModel.objects.get(
                        UserCategory='Customer',
                        UserMobileNo=strMobileNo,
                        UserPass=userPass
                    )
                    
                    # Django login
                    login(request, user_data.ULink)  # user_data.ULink is actual Django User model

                    # Store category also in session (for navbar)
                    request.session['userCategoryis'] = user_data.UserCategory

                    return redirect('taxi_app:home')
                
                except usersDataModel.DoesNotExist:
                    messages.warning(request, 'Invalid Mobile Number or Password.')
            else:
                messages.warning(request, 'Enter a valid 10-digit mobile number.')

        return render(request, 'login/cutomerLogin.html')

def developerLoginFunctionBaseView(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already login into BigTaxi, Developer Department '{}'".format(request.user.username))
        return redirect('taxi_app:home')

    else:
        if request.method == 'POST':
            userMobileNo = int(request.POST.get('mobileNo')); userPass = request.POST.get('password1')

            strMobileNo = str(userMobileNo)
            if userMobileNo and userPass and (len(strMobileNo) == 10):

                try:
                    user_data = usersDataModel.objects.get(
                        UserCategory='Developer',
                        UserMobileNo=strMobileNo,
                        UserPass=userPass
                    )
                    
                    # Django login
                    login(request, user_data.ULink)  # user_data.ULink is actual Django User model

                    # Store category also in session (for navbar)
                    request.session['userCategoryis'] = user_data.UserCategory

                    return redirect('taxi_app:home')
                
                except usersDataModel.DoesNotExist:
                    messages.warning(request, 'Invalid Mobile Number or Password.')
            else:
                messages.warning(request, 'Enter a valid 10-digit mobile number.')
            
        return render(request, 'login/developerLogin.html')

# Signup 
def driverSignUpFunctionBaseView(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already login into BigTaxi, Driver Department '{}'. Login out to create new account".format(request.user.username))
        return redirect('taxi_app:home')
    
    else:
        if request.method == "POST":
            # request.POST.get('')
            username = request.POST.get('username'); email = request.POST.get('gmail'); password1 = request.POST.get('password1'); password2 = request.POST.get('password2'); mobileNo = request.POST.get('mobileNo'); strMobileNo = str(mobileNo)
            vName = request.POST.get('vechicleName'); vCustomerLimit = abs(int(request.POST.get('vechiclePassengerLimit'))); vNo = request.POST.get('vechicleNo'); vType = request.POST.get('vehicleType')
            UDM = usersDataModel.objects.all(); continueData = True; userData = User.objects.all()

            for UD in userData:
                if str(UD.username) == str(username): continueData = False

            if continueData:
                for UDM1 in UDM:
                    if str(UDM1.UserMobileNo) == str(mobileNo): continueData = False

                if continueData:
                    if vCustomerLimit != 0:
                        if (vType in ['bicycle', 'motor bike']) and (vCustomerLimit == 1) or ((vType == '4 wheeler') and (vCustomerLimit <= 10)) or ((vType == 'more than 4 wheeler') and (vCustomerLimit <= 20)):
                            if (strMobileNo != '000000000') and (len(strMobileNo) == 10) and (int(strMobileNo[0]) in [6, 7, 8, 9]):
                                if password1 == password2:
                                    user = User.objects.create_user(username=username, email=email, password=password2)
                                    user.save()

                                    DMS = DriverModelStore.objects.all(); NotNameOneCustomer = 'BIGTAXIDEVELOPER'
                                    # CouponCode Name Define
                                    CodeName = 'BIGTAXIDRIVER'

                                    if len(DMS) > 0:
                                        codeLst, lstOfUsername = [DataCode.CouponCode for DataCode in DMS if DataCode.CouponCode != NotNameOneCustomer], [DataIn.DriverName.lower() for DataIn in DMS if DataIn.CouponCode != NotNameOneCustomer]
                                        lastCode = codeLst[len(codeLst) - 1]

                                        if request.user.username in lstOfUsername:
                                            messages.warning(request, "you can't create two coupon for one id, Try After 6 Month For New Id")

                                        else:
                                            oldCode = ''
                                            for LC in lastCode: 
                                                if LC.isdigit(): oldCode += LC
                                            newCode = CodeName + str((int(oldCode) + 1))

                                    else:
                                        Number = 10063; newCode = CodeName + str(Number)

                                    oldCodelst = usersDataModel.objects.all(); oldCodeData = [UD101.UserCode for UD101 in oldCodelst]; oldCodeBar = oldCodeData[len(oldCodeData) - 1]; oldNo = ''; nameOfCode = 'BIGTAXICODE'
                                    for OC in oldCodeBar:
                                        if OC.isdigit(): oldNo += OC
                                    newCodeNo = str(int(oldNo) + 1); successfullGenerateNewCode = nameOfCode + newCodeNo
                                    UDM = usersDataModel(ULink = user, UserCategory = 'Driver', UserMobileNo = mobileNo, UserPass = password2, CouponCode = newCode, UserCode = successfullGenerateNewCode)
                                    UDM.save()

                                    DriverModelStore(CouponCode = newCode, DriverName = username).save()

                                    driverDataModel(VUDM = UDM, VehicleName = vName, VehicleCustomerLimit = str(vCustomerLimit), Vehicle = vType, VehicleNo = vNo).save()
                                    messages.success(request ,'Successfully signup into \'BigTaxi\' driver department.')
                                    return render(request, 'signup/driverSignUp.html')
                                
                                else:
                                    messages.warning(request, 'Password is Not Matched!')
                                    return render(request, 'signup/driverSignUp.html')
                                
                            else:
                                messages.warning(request, 'Enter Correct Mobile No!, Again.')
                                return render(request, 'signup/driverSignUp.html')
                            
                        else:
                            messages.warning(request, '{} does not have right\'s to take {} passenger, read informations to signup!'.format(vType, vCustomerLimit))
                            return render(request, 'more/readinformations.html')
                    else:
                        messages.warning(request, 'Passeger limit is Zero. Then why you need to signup in driver department.')
                        return render(request, 'signup/driverSignUp.html')
                    
                else:
                    messages.warning(request, 'Mobile No, already Exist "{}".'.format(strMobileNo))
                    return render(request, 'signup/driverSignUp.html')
            else:
                messages.warning(request, "Username '{}' is already exist inside system.".format(username))
                return render(request, 'signup/driverSignUp.html')
        
        return render(request, 'signup/driverSignUp.html')

def customerSignUpFunctionBaseView(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already login into BigTaxi, Customer Department '{}'. Login out to create new account".format(request.user.username))
        return redirect('taxi_app:home')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username'); email = request.POST.get('gmail'); password1 = request.POST.get('password1'); password2 = request.POST.get('password2'); mobileNo = request.POST.get('mobileNo'); strMobileNo = str(mobileNo)
            UDM = usersDataModel.objects.all(); continueData = True; userData = User.objects.all()

            for UD in userData:
                if str(UD.username) == str(username): continueData = False

            if continueData:
                for UDM1 in UDM:
                    if str(UDM1.UserMobileNo) == str(mobileNo): continueData = False

                if continueData:
                    if (strMobileNo != '000000000') and (len(strMobileNo) == 10) and (int(strMobileNo[0]) in [6, 7, 8, 9]):
                        if password1 == password2:
                            user = User.objects.create_user(username=username, email=email, password=password2)
                            user.save()

                            oldCodelst = usersDataModel.objects.all(); oldCodeData = [UD101.UserCode for UD101 in oldCodelst]; oldCodeBar = oldCodeData[len(oldCodeData) - 1]; oldNo = ''; nameOfCode = 'BIGTAXICODE'
                            for OC in oldCodeBar:
                                if OC.isdigit(): oldNo += OC
                            newCodeNo = str(int(oldNo) + 1); successfullGenerateNewCode = nameOfCode + newCodeNo
                            UDM = usersDataModel(ULink = user, UserCategory = 'Customer', UserMobileNo = mobileNo, UserPass = password2, CouponCode = 'BIGTAXICUSTOMER', UserCode = successfullGenerateNewCode)
                            UDM.save()

                            messages.success(request, 'Successfully signup into \'BigTaxi\' customer department')
                            return render(request, 'signup/cutomerSignUp.html')
                        
                        else:
                            messages.warning(request, 'Password is Not Matched!')
                            return render(request, 'signup/cutomerSignUp.html')
                    else:
                        messages.warning(request, 'Enter Correct Mobile No!, Again.')
                        return render(request, 'signup/cutomerSignUp.html')
                else:
                    messages.warning(request, 'Mobile No, already Exist "{}"'.format(strMobileNo))
                    return render(request, 'signup/cutomerSignUp.html')
            else:
                messages.warning(request, "Username '{}' is already exist inside system".format(username))
                return render(request, 'signup/cutomerSignUp.html')

        return render(request, 'signup/cutomerSignUp.html')

def developerSignUpFunctionBaseView(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already login into BigTaxi, Developer Department '{}'. Login out to create new account".format(request.user.username))
        return redirect('taxi_app:home')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username'); email = request.POST.get('gmail'); password1 = request.POST.get('password1'); password2 = request.POST.get('password2'); mobileNo = request.POST.get('mobileNo'); sc = request.POST.get('secretCode'); strMobileNo = str(mobileNo)
            # Big Taxi PersonalCode Secret Granted Successfull, change after every 6 months
            secretCode = 'BIGTAXIMUOD106463SECRETGS'
            UDM = usersDataModel.objects.all(); continueData = True; userData = User.objects.all()

            for UD in userData:
                if str(UD.username) == str(username): continueData = False

            if continueData:
                for UDM1 in UDM:
                    if str(UDM1.UserMobileNo) == str(mobileNo): continueData = False

                if continueData:
                    if sc == secretCode:
                        if (strMobileNo != '000000000') and (len(strMobileNo) == 10) and (int(strMobileNo[0]) in [6, 7, 8, 9]):
                            if password1 == password2:
                                user = User.objects.create_user(username=username, email=email, password=password2)
                                user.save()

                                DMS = DriverModelStore.objects.all(); NotNameOneCustomer = 'BIGTAXIDRIVER'
                                # CouponCode Name Define
                                CodeName = 'BIGTAXIDEVELOPER'

                                if len(DMS) > 0:
                                    codeLst, lstOfUsername = [DataCode.CouponCode for DataCode in DMS if DataCode.CouponCode != NotNameOneCustomer], [DataIn.DriverName.lower() for DataIn in DMS if DataIn.CouponCode != NotNameOneCustomer]
                                    lastCode = codeLst[len(codeLst) - 1]

                                    if request.user.username in lstOfUsername:
                                        messages.warning(request, "you can't create two coupon for one id, Try After 6 Month For New Id")

                                    else:
                                        oldCode = ''
                                        for LC in lastCode: 
                                            if LC.isdigit(): oldCode += LC
                                        newCode = CodeName + str((int(oldCode) + 1))

                                else:
                                    Number = 50064; newCode = CodeName + str(Number)

                                oldCodelst = usersDataModel.objects.all(); oldCodeData = [UD101.UserCode for UD101 in oldCodelst]; oldCodeBar = oldCodeData[len(oldCodeData) - 1]; oldNo = ''; nameOfCode = 'BIGTAXICODE'
                                for OC in oldCodeBar:
                                    if OC.isdigit(): oldNo += OC
                                newCodeNo = str(int(oldNo) + 1); successfullGenerateNewCode = nameOfCode + newCodeNo
                                UDM = usersDataModel(ULink = user, UserCategory = 'Developer', UserMobileNo = mobileNo, UserPass = password2, CouponCode = newCode, UserCode = successfullGenerateNewCode)
                                UDM.save()

                                DriverModelStore(CouponCode = newCode, DriverName = username).save()
                                messages.success(request, 'Successfully signup into \'BigTaxi\' developer department')
                                # return render(request, 'signup/developerSignUp.html')
                                # http://localhost:8000/ls/driver/signup/ : url bug
                                return redirect('driver:inforamtion')
                            
                            else:
                                messages.warning(request, 'Password is Not Matched!')
                                return render(request, 'signup/developerSignUp.html')
                        else:
                            messages.warning(request, 'Enter Correct Mobile No!, Again.')
                            return render(request, 'signup/developerSignUp.html')
                    else:
                        messages.warning(request, 'Secrect Code Is Not Matched For Developer Tools Login')
                        return render(request, 'signup/developerSignUp.html')
                else:
                    messages.warning(request, 'Mobile No, already Exist "{}"'.format(strMobileNo))
                    return render(request, 'signup/developerSignUp.html')
            else:
                messages.warning(request, "Username '{}' is already exist inside system".format(username))
                return render(request, 'signup/developerSignUp.html')

    return render(request, 'signup/developerSignUp.html')

def moreInformationsFunctionBaseView(request):
    messages.warning(request, 'error is to check, vechicle informations')
    return render(request, 'more/readInformations.html')

def pageNotFoundFunctionsBaseView(request):
    return render(request, 'more/pageNotFound.html')

# logout Function
def logOutPageFunctionBaseView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect('taxi_app:lan')
        return render(request, 'logOut.html')
    else:
        return render(request, 'more/pageNotFound.html')