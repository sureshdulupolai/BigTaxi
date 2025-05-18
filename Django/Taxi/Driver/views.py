from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Driver.models import driverDataModel, DriverModelStore
from Users.models import usersDataModel
from Customer.models import cutomerDataModel

# login
def driverLoginFunctionBaseView(request):
    if request.method == 'POST':
        UDM = usersDataModel.objects.filter(UserCategory = 'Driver')
        userMobileNo = int(request.POST.get('mobileNo')); userPass = request.POST.get('password1')

        strMobileNo = str(userMobileNo)
        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and (strMobileNo[0] in [6, 7, 8, 9]):

            DataGet = False

            for UDMData in UDM:
                if (int(UDMData.UserMobileNo) == userMobileNo) and (str(UDMData.UserPass) == str(userPass)): DataGet = True
                else: continue

            if DataGet:
                return HttpResponse('Driver Login Successfull')
            
            else:messages.warning(request, 'No User Found in Driver!, for more details contact us')
        
        else:messages.warning(request, 'Enter Correct Mobile No!, Again.')

    return render(request, 'login/driverLogin.html')

def customerLoginFunctionBaseView(request):
    if request.method == 'POST':
        UDM = usersDataModel.objects.filter(UserCategory = 'Customer')
        userMobileNo = int(request.POST.get('mobileNo')); userPass = request.POST.get('password1')

        strMobileNo = str(userMobileNo)
        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and (strMobileNo[0] in [6, 7, 8, 9]):

            DataGet = False

            for UDMData in UDM:
                if (int(UDMData.UserMobileNo) == userMobileNo) and (str(UDMData.UserPass) == str(userPass)): DataGet = True
                else: continue

            if DataGet:
                return HttpResponse('Customer Login Successfull')
            else:messages.warning(request, 'No User Found in Customer!, for more details contact us')
        
        else:messages.warning(request, 'Enter Correct Mobile No!, Again.')

    return render(request, 'login/cutomerLogin.html')

def developerLoginFunctionBaseView(request):
    if request.method == 'POST':
        UDM = usersDataModel.objects.filter(UserCategory = 'Developer')
        userMobileNo = int(request.POST.get('mobileNo')); userPass = request.POST.get('password1')

        strMobileNo = str(userMobileNo)
        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and (strMobileNo[0] in [6, 7, 8, 9]):

            DataGet = False

            for UDMData in UDM:
                if (int(UDMData.UserMobileNo) == userMobileNo) and (str(UDMData.UserPass) == str(userPass)): DataGet = True
                else: continue

            if DataGet:
                return HttpResponse('Developer Login Successfull')
            
            else:messages.warning(request, 'No User Found in Developer!, for more details contact us')
        
        else:messages.warning(request, 'Enter Correct Mobile No!, Again.')
        
    return render(request, 'login/developerLogin.html')



# Signup 
def driverSignUpFunctionBaseView(request):
    if request.method == "POST":
        # request.POST.get('')
        username = request.POST.get('username'); email = request.POST.get('gmail'); password1 = request.POST.get('password1'); password2 = request.POST.get('password2'); mobileNo = request.POST.get('mobileNo'); strMobileNo = str(mobileNo)
        vName = request.POST.get('vechicleName'); vCustomerLimit = request.POST.get('vechiclePassengerLimit'); vNo = request.POST.get('vechicleNo'); vType = request.POST.get('vehicleType')

        print('Username : ', username)
        print('Gmail : ', email)
        print('Pass One : ', password1)
        print('Pass Two : ', password2)
        print('Mobile No : ', mobileNo)
        print('Vechicle Name : ', vName)
        print('Vechicle Passeneger Limit : ', vCustomerLimit)
        print('Vechicle No : ', vNo)
        print('Vechicle Type : ', vType)

        # if (strMobileNo != '000000000') and (len(strMobileNo) == 10) and strMobileNo[0] in [6, 7, 8, 9]:
        #     if password1 == password2:
        #         user = User.objects.create_user(username=username, email=email, password=password2)
        #         user.save()

        #         DMS = DriverModelStore.objects.all(); NotNameOneCustomer = 'BIGTAXIDEVELOPER'
        #         # CouponCode Name Define
        #         CodeName = 'BIGTAXIDRIVER'

        #         if len(DMS) > 0:
        #             codeLst, lstOfUsername = [DataCode.CouponCode for DataCode in DMS if DataCode.CouponCode != NotNameOneCustomer], [DataIn.DriverName.lower() for DataIn in DMS if DataIn.CouponCode != NotNameOneCustomer]
        #             lastCode = codeLst[len(codeLst) - 1]

        #             if request.user.username in lstOfUsername:
        #                 messages.warning(request, "you can't create two coupon for one id, Try After 6 Month For New Id")

        #             else:
        #                 oldCode = ''
        #                 for LC in lastCode: 
        #                     if LC.isdigit(): oldCode += LC
        #                 newCode = CodeName + str((int(oldCode) + 1))

        #         else:
        #             Number = 10063; newCode = CodeName + str(Number)

        #         UDM = usersDataModel(ULink = user, UserCategory = 'Driver', UserMobileNo = mobileNo, UserPass = password2, CouponCode = newCode)
        #         UDM.save()

        #         DriverModelStore(CouponCode = newCode, DriverName = username).save()

        #         driverDataModel(VUDM = UDM, VehicleName = vName, VehicleCustomerLimit = vCustomerLimit, Vehicle = vType, VehicleNo = vNo).save()

        #     else:
        #         messages.warning(request, 'Password is Not Matched!')
        # else:
        #     messages.warning(request, 'Enter Correct Mobile No!, Again.')
    
    return render(request, 'signup/driverSignUp.html')

def customerSignUpFunctionBaseView(request):
    if request.method == 'POST':
        username = request.POST.get('username'); email = request.POST.get('gmail'); password1 = request.POST.get('password1'); password2 = request.POST.get('password2'); mobileNo = request.POST.get('mobileNo'); strMobileNo = str(mobileNo)
        
        if (strMobileNo != '000000000') and (len(strMobileNo) == 10) and strMobileNo[0] in [6, 7, 8, 9]:
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save()

                UDM = usersDataModel(ULink = user, UserCategory = 'Customer', UserMobileNo = mobileNo, UserPass = password2, CouponCode = 'BIGTAXICUSTOMER')
                UDM.save()

                cutomerDataModel(UDM = UDM).save()
            else:
                messages.warning(request, 'Password is Not Matched!')
        else:
            messages.warning(request, 'Enter Correct Mobile No!, Again.')
    
    return render(request, 'signup/cutomerSignUp.html')

def developerSignUpFunctionBaseView(request):
    if request.method == 'POST':
        username = request.POST.get('username'); email = request.POST.get('gmail'); password1 = request.POST.get('password1'); password2 = request.POST.get('password2'); mobileNo = request.POST.get('mobileNo'); sc = request.POST.get('secretCode'); strMobileNo = str(mobileNo)
        # Big Taxi PersonalCode Secret Granted Successfull, change after every 6 months
        secretCode = 'BIGTAXIMUOD106463SECRETGS'
        
        if sc == secretCode:
            if (strMobileNo != '000000000') and (len(strMobileNo) == 10) and strMobileNo[0] in [6, 7, 8, 9]:
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

                    UDM = usersDataModel(ULink = user, UserCategory = 'Developer', UserMobileNo = mobileNo, UserPass = password2, CouponCode = newCode)
                    UDM.save()

                    DriverModelStore(CouponCode = newCode, DriverName = username).save()
            
                else:
                    messages.warning(request, 'Password is Not Matched!')
            else:
                messages.warning(request, 'Enter Correct Mobile No!, Again.')
        else:
            messages.warning(request, 'Secrect Code Is Not Matched For Developer Tools Login')

    return render(request, 'signup/developerSignUp.html')