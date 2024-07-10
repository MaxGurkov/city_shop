from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q  # Импортируем Q для построения запросов

# Базовый класс с общим методом list
class BaseViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StreetViewSet(BaseViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            city = request.query_params.get('city', None)
            street = request.query_params.get('street', None)
            open_status = request.query_params.get('open', None)

            if city:
                queryset = queryset.filter(city__name=city)
            if street:
                queryset = queryset.filter(street__name=street)
            if open_status is not None:
                now = timezone.localtime().time()
                if open_status == '1':
                    queryset = queryset.filter(opening_time__lte=now, closing_time__gte=now)
                else:
                    queryset = queryset.filter(Q(opening_time__gte=now) | Q(closing_time__lte=now))

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
