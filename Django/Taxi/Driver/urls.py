from django.urls import path
from Driver import views

app_name = 'driver'

urlpatterns = [
    # SignUp Path
    path('signup/', views.customerSignUpFunctionBaseView, name='customerSignup'),
    path('driver/signup/', views.driverSignUpFunctionBaseView, name='driverSignup'),
    path('developer/signup/', views.developerSignUpFunctionBaseView, name='developerSigup'),

    # Login Path
    path('login/', views.customerLoginFunctionBaseView, name='customerLogin'),
    path('driver/login/', views.driverLoginFunctionBaseView, name='driverLogin'),
    path('developer/login/', views.developerLoginFunctionBaseView, name='developerLogin'),

    path('more-information/', views.moreInformationsFunctionBaseView, name='inforamtion'),
    path('page-not-found/', views.pageNotFoundFunctionsBaseView, name='pageNotFound'),

    path('log-out/', views.logOutPageFunctionBaseView, name='logOut'),
]