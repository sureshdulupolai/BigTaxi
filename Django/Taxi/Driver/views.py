from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Driver.models import driverDataModel

# login
def driverLoginFunctionBaseView(request):
    return render(request, 'login/driverLogin.html')

def customerLoginFunctionBaseView(request):
    return render(request, 'login/cutomerLogin.html')

def developerLoginFunctionBaseView(request):
    return render(request, 'login/developerLogin.html')

# Signup 
def driverSignUpFunctionBaseView(request):
    # if request.method == "POST":
        # request.POST.get('')
    username = 'rahul'
    email = 'rahul@gmail.com'
    password1 = 'krish123'
    password2 = 'krish123'
    mobileNo = 9820646838
    
    if password1 == password2:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password2
        )

        user.save()

        driverDataModel(
            ULink = user,
            UserMobileNo = mobileNo,
            UserCategory = 'Driver',
        ).save()

    else:
        messages.warning(
            request, 'Password is Not Matched!'
        )
    
    return render(request, 'signup/driverSignUp.html')

def customerSignUpFunctionBaseView(request):
    return render(request, 'signup/cutomerSignUp.html')

def developerSignUpFunctionBaseView(request):
    return render(request, 'signup/developerSignUp.html')