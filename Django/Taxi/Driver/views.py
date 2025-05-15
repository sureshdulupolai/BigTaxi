from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Driver.models import driverDataModel
from Users.models import usersDataModel
from Customer.models import cutomerDataModel

# login
def driverLoginFunctionBaseView(request):
    if request.method == 'POST':
        UDM = usersDataModel.objects.filter(UserCategory = 'Driver')
        userMobileNo = int(request.POST.get('mobileNo'))
        userPass = request.POST.get('userPassword')

        strMobileNo = str(userMobileNo)
        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and (strMobileNo[0] in [6, 7, 8, 9]):

            DataGet = False

            for UDMData in UDM:
                if (int(UDMData.UserMobileNo) == userMobileNo) and (str(UDMData.UserPass) == str(userPass)): DataGet = True
                else: continue

            if DataGet:
                # return to home page with login
                pass
            else:messages.warning(request, 'No User Found in Driver!, for more details contact us')
        
        else:messages.warning(request, 'Enter Correct Mobile No!, Again.')

    return render(request, 'login/driverLogin.html')

def customerLoginFunctionBaseView(request):
    if request.method == 'POST':
        UDM = usersDataModel.objects.filter(UserCategory = 'Customer')
        userMobileNo = int(request.POST.get('mobileNo'))
        userPass = request.POST.get('userPassword')

        strMobileNo = str(userMobileNo)
        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and (strMobileNo[0] in [6, 7, 8, 9]):

            DataGet = False

            for UDMData in UDM:
                if (int(UDMData.UserMobileNo) == userMobileNo) and (str(UDMData.UserPass) == str(userPass)): DataGet = True
                else: continue

            if DataGet:
                # return to home page with login
                pass
            else:messages.warning(request, 'No User Found in Customer!, for more details contact us')
        
        else:messages.warning(request, 'Enter Correct Mobile No!, Again.')

    return render(request, 'login/cutomerLogin.html')

def developerLoginFunctionBaseView(request):
    if request.method == 'POST':
        UDM = usersDataModel.objects.filter(UserCategory = 'Developer')
        userMobileNo = int(request.POST.get('mobileNo'))
        userPass = request.POST.get('userPassword')

        strMobileNo = str(userMobileNo)
        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and (strMobileNo[0] in [6, 7, 8, 9]):

            DataGet = False

            for UDMData in UDM:
                if (int(UDMData.UserMobileNo) == userMobileNo) and (str(UDMData.UserPass) == str(userPass)): DataGet = True
                else: continue

            if DataGet:
                # return to home page with login
                pass
            else:messages.warning(request, 'No User Found in Developer!, for more details contact us')
        
        else:messages.warning(request, 'Enter Correct Mobile No!, Again.')
        
    return render(request, 'login/developerLogin.html')



# Signup 
def driverSignUpFunctionBaseView(request):
    if request.method == "POST":
        # request.POST.get('')
        username = 'sonu'; email = 'sonu@gmail.com'; password1 = 'krish123'; password2 = 'krish123'; mobileNo = 9820646789
        strMobileNo = str(mobileNo)

        if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and strMobileNo[0] in [6, 7, 8, 9]:
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save()

                UDM = usersDataModel(ULink = user, UserCategory = 'Driver', UserMobileNo = mobileNo, UserPass = password2)
                UDM.save()

                driverDataModel(VUDM = UDM, VehicleName = 'BMW', VehicleCustomerLimit = 4, Vehicle = '4 Wheeler Car', VehicleNo = 'MH 03 2006').save()

            else:
                messages.warning(request, 'Password is Not Matched!')
        else:
            messages.warning(request, 'Enter Correct Mobile No!, Again.')
    
    return render(request, 'signup/driverSignUp.html')

def customerSignUpFunctionBaseView(request):
    username = 'ashish'; email = 'ashish@gmail.com'; password1 = 'krish123'; password2 = 'krish123'; mobileNo = 9820646901
    strMobileNo = str(mobileNo)
    
    if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and strMobileNo[0] in [6, 7, 8, 9]:
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password2)
            user.save()

            UDM = usersDataModel(ULink = user, UserCategory = 'Customer', UserMobileNo = mobileNo, UserPass = password2)
            UDM.save()

            cutomerDataModel(UDM = UDM).save()
        else:
            messages.warning(request, 'Password is Not Matched!')
    else:
        messages.warning(request, 'Enter Correct Mobile No!, Again.')
    
    return render(request, 'signup/cutomerSignUp.html')

def developerSignUpFunctionBaseView(request):
    username = 'ashish'; email = 'ashish@gmail.com'; password1 = 'krish123'; password2 = 'krish123'; mobileNo = 9820646901
    strMobileNo = str(mobileNo)
    
    if (strMobileNo == '000000000') and (len(strMobileNo) == 10) and strMobileNo[0] in [6, 7, 8, 9]:
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password2)
            user.save()

            UDM = usersDataModel(ULink = user, UserCategory = 'Developer', UserMobileNo = mobileNo, UserPass = password2)
            UDM.save()
    
        else:
            messages.warning(request, 'Password is Not Matched!')
    else:
        messages.warning(request, 'Enter Correct Mobile No!, Again.')

    return render(request, 'signup/developerSignUp.html')