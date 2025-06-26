from django.urls import path
from .views import (
    TaxiBarCodeList,
    PinTaxiAvailableList,
    TaxiTimeOverList,
    TaxiOnFinishList,
    ReviewAndRatingList,
    ReviewBarcodeList,
    ReviewDeleteList,
    ErrorWorkList,
)

urlpatterns = [
    path('api/barcodes/', TaxiBarCodeList.as_view()),
    path('api/pin-taxi/', PinTaxiAvailableList.as_view()),
    path('api/taxi-time-over/', TaxiTimeOverList.as_view()),
    path('api/taxi-finished/', TaxiOnFinishList.as_view()),

    path('reviews/', ReviewAndRatingList.as_view(), name='review-and-rating'),
    path('review-barcodes/', ReviewBarcodeList.as_view(), name='review-barcode'),
    path('review-delete/', ReviewDeleteList.as_view(), name='review-delete'),
    path('error-works/', ErrorWorkList.as_view(), name='error-work'),
]
