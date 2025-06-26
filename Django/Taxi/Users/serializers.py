from rest_framework import serializers
from Users.models import ReviewAndRating, ReviewBarcode, ReviewDelete, ErrorWork

class ReviewAndRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAndRating
        fields = '__all__'

class ReviewBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBarcode
        fields = '__all__'

class ReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewDelete
        fields = '__all__'

class ErrorWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorWork
        fields = '__all__'
