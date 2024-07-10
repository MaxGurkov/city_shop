from rest_framework import serializers
from .models import City, Street, Shop

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')
    street = serializers.SlugRelatedField(queryset=Street.objects.all(), slug_field='name')

    class Meta:
        model = Shop
        fields = '__all__'

    def create(self, validated_data):
        city_name = validated_data.pop('city')
        street_name = validated_data.pop('street')

        city = City.objects.get(name=city_name)
        street = Street.objects.get(name=street_name, city=city)

        shop = Shop.objects.create(city=city, street=street, **validated_data)
        return shop
