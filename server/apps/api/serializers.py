import json
from rest_framework import serializers
from .models import User, Clothes, ClothesSet, ClothesSetReview

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nickname', 'gender', 'birthday']
        extra_kwargs = {'password': {'write_only': True}}


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ('id', 'upper_category', 'lower_category', 'image_url', 'alias', 'owner')
        read_only_fields = ('owner', )


class ClothesSetSerializer(serializers.ModelSerializer):
    clothes = serializers.PrimaryKeyRelatedField(many=True, queryset=Clothes.objects.all())
    
    class Meta:
        model = ClothesSet
        fields = ('id', 'clothes', 'name', 'style', 'image_url', 'owner')
        read_only_fields = ('owner', )
        
class ClothesSetReadSerializer(serializers.ModelSerializer):
    clothes = ClothesSerializer(many=True)
    
    class Meta:
        model = ClothesSet
        fields = ('id', 'clothes', 'name', 'style', 'image_url', 'owner')
        read_only_fields = ('owner', )
        
class ClothesSetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesSetReview
        fields = ('id', 'clothes_set', 'start_datetime', 'end_datetime', 
                  'location', 'review', 'max_temp', 'min_temp', 
                  'max_sensible_temp', 'min_sensible_temp', 'humidity', 
                  'wind_speed', 'precipitation', 'comment', 'weather_type', 'owner')
        read_only_fields = ('owner', )

class ClothesSetReviewReadSerializer(serializers.ModelSerializer):
    clothes_set = ClothesSetReadSerializer()
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        with open('apps/api/locations/data.json') as json_file:
            json_data = json.load(json_file)
        ret['location'] = json_data[str(ret['location'])]['full_address']
        
        return ret
    
    class Meta:
        model = ClothesSetReview
        fields = ('id', 'clothes_set', 'start_datetime', 'end_datetime', 
                  'location', 'review', 'max_temp', 'min_temp', 
                  'max_sensible_temp', 'min_sensible_temp', 'humidity', 
                  'wind_speed', 'precipitation', 'comment', 'owner')
        
