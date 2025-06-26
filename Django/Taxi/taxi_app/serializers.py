from rest_framework import serializers
from .models import TaxiBarCode, PinTaxiAvailable, TaxiTimeOver, TaxiOnFinish, TaxiOnRunning

class TaxiBarCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiBarCode
        fields = '__all__'

class PinTaxiAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinTaxiAvailable
        fields = '__all__'

class TaxiTimeOverSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiTimeOver
        fields = '__all__'

class TaxiOnFinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiOnFinish
        fields = '__all__'

class TaxiOnRunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiOnRunning
        fields = '__all__'