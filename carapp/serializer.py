from rest_framework import serializers
from .models import *

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMerch
        fields = ('username', 'email', 'password','date_joined','is_admin','is_active','is_staff','is_superuser','last_login')
class SpareSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = ('namePart', 'price','ImagePart','Phone','categoryPart','categoryImage','locationPart')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = CarCategory
       fields = ('categoryPart', 'categoryImage', 'categoryName')