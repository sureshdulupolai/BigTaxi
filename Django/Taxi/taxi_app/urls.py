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

    # review page
    path('review/', views.reviewPageFunctionBaseView, name='review'),
    path('delete-review/', views.deleteReviewFunctionBaseView, name='deleteReview'),
]