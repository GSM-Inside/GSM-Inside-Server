from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
from gallery.serializers import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

        extra_kwargs = {
            'post': {'required': False}
        }


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

        extra_kwargs = {
            'like': {'read_only': True},
            'dislike': {'read_only': True},
            'is_admin': {'read_only': True},
            'password': {'write_only': True, 'min_length': 4},
            'date': {'read_only': True},
        }

    def create(self, validated_data):
        if not 'images' in validated_data:
            post = Post.objects.create(**validated_data)
        else:
            image = validated_data.pop('images')
            post = Post.objects.create(**validated_data)
            for i in image:
                Image.objects.create(post=post, **i)

        return post

    def update(self, instance, validated_data):
        if 'gallery' in validated_data:
            raise ValidationError()
        image = validated_data.pop('images')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.images.all().delete()
        for i in image:
            Image.objects.create(post=instance, **i)
        return instance


class PostTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'gallery', 'like')
