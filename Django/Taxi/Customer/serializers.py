from rest_framework import serializers
from Customer.models import repostData, SaveNotificaionDeletePin, PinDeleteReview

class repostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = repostData
        fields = '__all__'

class SaveNotificaionDeletePinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveNotificaionDeletePin
        fields = '__all__'

class PinDeleteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinDeleteReview
        fields = '__all__'
