from django.shortcuts import render

# login
def driverLoginFunctionBaseView(request):
    return render(request, 'login/driverLogin.html')

def customerLoginFunctionBaseView(request):
    return render(request, 'login/cutomerLogin.html')

def developerLoginFunctionBaseView(request):
    return render(request, 'login/developerLogin.html')

# Signup 
def driverSignUpFunctionBaseView(request):
    return render(request, 'signup/driverSignUp.html')

def customerSignUpFunctionBaseView(request):
    return render(request, 'signup/cutomerSignUp.html')

def developerSignUpFunctionBaseView(request):
    return render(request, 'signup/developerSignUp.html')