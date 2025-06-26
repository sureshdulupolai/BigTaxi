from rest_framework import generics
from taxi_app.models import TaxiBarCode, PinTaxiAvailable, TaxiTimeOver, TaxiOnFinish
from taxi_app.serializers import (
    TaxiBarCodeSerializer,
    PinTaxiAvailableSerializer,
    TaxiTimeOverSerializer,
    TaxiOnFinishSerializer
)

from Users.models import ReviewAndRating, ReviewBarcode, ReviewDelete, ErrorWork
from Users.serializers import (
    ReviewAndRatingSerializer,
    ReviewBarcodeSerializer,
    ReviewDeleteSerializer,
    ErrorWorkSerializer
)

class TaxiBarCodeList(generics.ListAPIView):
    queryset = TaxiBarCode.objects.all()
    serializer_class = TaxiBarCodeSerializer

class PinTaxiAvailableList(generics.ListAPIView):
    queryset = PinTaxiAvailable.objects.all()
    serializer_class = PinTaxiAvailableSerializer

class TaxiTimeOverList(generics.ListAPIView):
    queryset = TaxiTimeOver.objects.all()
    serializer_class = TaxiTimeOverSerializer

class TaxiOnFinishList(generics.ListAPIView):
    queryset = TaxiOnFinish.objects.all()
    serializer_class = TaxiOnFinishSerializer

class ReviewAndRatingList(generics.ListAPIView):
    queryset = ReviewAndRating.objects.all()
    serializer_class = ReviewAndRatingSerializer

class ReviewBarcodeList(generics.ListAPIView):
    queryset = ReviewBarcode.objects.all()
    serializer_class = ReviewBarcodeSerializer

class ReviewDeleteList(generics.ListAPIView):
    queryset = ReviewDelete.objects.all()
    serializer_class = ReviewDeleteSerializer

class ErrorWorkList(generics.ListAPIView):
    queryset = ErrorWork.objects.all()
    serializer_class = ErrorWorkSerializer
