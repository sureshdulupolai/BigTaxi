from rest_framework import generics
from taxi_app.models import TaxiBarCode, PinTaxiAvailable, TaxiTimeOver, TaxiOnFinish
from taxi_app.serializers import (
    TaxiBarCodeSerializer,
    PinTaxiAvailableSerializer,
    TaxiTimeOverSerializer,
    TaxiOnFinishSerializer
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
