from rest_framework import serializers
from .models import CarMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMerch
        fields = ('name', 'description', 'price')
# class MerchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpareParts
#         fields = (' nameChoose', 'namePart', 'price','locationChoose',' ImagePar',' Phone','carCat')

# class MerchSerializer(serializers.ModelSerializer):
#     class Meta:
#        model = CarCategory
#         fields = ('categoryPart', 'categoryImage', 'categoryName')