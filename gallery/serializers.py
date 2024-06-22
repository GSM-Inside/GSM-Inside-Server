from rest_framework import serializers
from .models import *


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

        extra_kwargs = {
            'view': {'read_only': True},
        }


class GalleryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryRequest
        fields = '__all__'

        extra_kwargs = {
            'status': {'read_only': True},
            'is_active': {'read_only': True},
        }
