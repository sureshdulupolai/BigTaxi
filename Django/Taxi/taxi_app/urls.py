from django.urls import path
from taxi_app import views

app_name = 'taxi_app'

urlpatterns = [
    # basic login
    path('', views.redirect_based_on_location, name='autoRedirect'),
    path('location/', views.locationPageFunctionViewBase, name='lan'),
    path('pin/', views.HomePageForTaxiAppViewFunction, name='home'),

    # pin taxi
    path('pin-taxi/', views.pinTaxiFunctionBaseView, name='pinTaxi'),
    path('pin-detail/<barCode>/', views.pinDetailFunctionBaseView, name='pinDetail'),
    path('pin-report/<barCodes>/', views.reportDriverOnPinTaxiFunctionBaseView, name='pinReport'),
    path('pin-report-check/<barCodeId>/', views.checkPinTaxiReportFunctionBaseView, name='checkPinReport'),
    path('delete-report-detail/<codeNeed>/', views.deletePinTaxiReport, name='deletePinTaxiReport'),
    path('delete-pin-detail/<codeNeed>/', views.deletePinTaxiDetailsNoReport, name='deletePinTaxiDetail'),

    # review page
    path('review/', views.reviewPageFunctionBaseView, name='review'),
    path('delete-review/', views.deleteReviewFunctionBaseView, name='deleteReview'),

]