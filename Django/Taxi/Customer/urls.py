from django.urls import path
from .views import (
    TaxiBarCodeList,
    PinTaxiAvailableList,
    TaxiTimeOverList,
    TaxiOnFinishList
)

urlpatterns = [
    path('api/barcodes/', TaxiBarCodeList.as_view()),
    path('api/pin-taxi/', PinTaxiAvailableList.as_view()),
    path('api/taxi-time-over/', TaxiTimeOverList.as_view()),
    path('api/taxi-finished/', TaxiOnFinishList.as_view()),
]
