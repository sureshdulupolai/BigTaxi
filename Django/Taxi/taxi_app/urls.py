from django.urls import path
from taxi_app import views

app_name = 'taxi_app'

urlpatterns = [
    # basic login
    path('', views.redirect_based_on_location, name='autoRedirect'),
    path('location/', views.locationPageFunctionViewBase, name='lan'),
    path('in/', views.HomePageForTaxiAppViewFunction, name='home'),

    # pin taxi
    path('pin/', views.pinTaxiFunctionBaseView, name='pinTaxi'),
    path('pin-detail/<barCode>/', views.pinDetailFunctionBaseView, name='pinDetail'),
    path('pin-status/<IdCodeNeed>/', views.checkStatusOfPinFunctionBaseView, name='pinStatus'),
    path('pin-report/<barCodes>/', views.reportDriverOnPinTaxiFunctionBaseView, name='pinReport'),
    path('pin-report-check/<barCodeId>/', views.checkPinTaxiReportFunctionBaseView, name='checkPinReport'),
    path('pin-report-delete/<codeNeed>/', views.deletePinTaxiReport, name='deletePinTaxiReport'),
    path('pin-detail-delete/<codeNeed>/', views.deletePinTaxiDetailsNoReport, name='deletePinTaxiDetail'),
    path('pin-repost/<CodeNeed>/', views.RePostPinTaxiFunctionBaseView, name='repostPin'),

    #
    path('status/', views.driverPinStartFunctionBaseView, name='statusDriverHere'),
    path('ready-to-go/<idCode>/', views.readyToGoFunctionBaseView, name='readyToGo'),

    # Customer
    path('ready-to-go-otp/<TaxiId>/', views.OtpPageFunctionBaseView, name='OTP'),
    path('ready-to-go-otpr/<idCode>/', views.ResendOtpFunctionBaseView, name='resendOTP'),
    path('status-verify/<idCode>/', views.runningPageFunctionBaseView, name='runningStatusVerify'),
    path('status-customer/', views.RunningStatusWithOTPCheckByCustomer, name='statusCustomer'),
    path('trip-continue/<IdCodeHere>/', views.liveRunningStatus, name='liveTaxiRunning'),

    # review page
    path('review/', views.reviewPageFunctionBaseView, name='review'),
    path('delete-review/', views.deleteReviewFunctionBaseView, name='deleteReview'),

    # testing code
    path('otp-testing/', views.PageFunctionHereForDemoTesting, name='tesing'),

    #
]