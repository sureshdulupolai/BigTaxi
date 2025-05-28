from django.urls import path
from taxi_app import views

app_name = 'taxi_app'

urlpatterns = [
    path('', views.redirect_based_on_location, name='autoRedirect'),
    path('pin/', views.HomePageForTaxiAppViewFunction, name='home'),
    path('pin-detail/<barCode>/', views.pinDetailFunctionBaseView, name='pinDetail'),
    path('pin-report/<barCodes>/', views.reportDriverOnPinTaxiFunctionBaseView, name='pinReport'),
    path('pin-report-check/<barCodeId>/', views.checkPinTaxiReportFunctionBaseView, name='checkPinReport'),
    path('review/', views.reviewPageFunctionBaseView, name='review'),
    path('delete-review/', views.deleteReviewFunctionBaseView, name='deleteReview'),
    path('pin-taxi/', views.pinTaxiFunctionBaseView, name='pinTaxi'),
    path('location/', views.locationPageFunctionViewBase, name='lan'),
]