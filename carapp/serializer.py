from rest_framework import serializers
from .models import CarMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMerch
        fields = ('name', 'description', 'price')