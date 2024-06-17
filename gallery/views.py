from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models import Post
from .serializers import *
from .models import *


# Create your views here.
class GalleryView(APIView):
    def get(self, request: object) -> Response:
        query = request.query_params.get('orderby', None)
        if query == 'latest':
            obj = Post.objects.filter(gallery=self).order_by('-date').gallery
            serializer = GallerySerializer(instance=obj, many=True)
        elif query == 'fame':
            obj = Post.objects.filter(gallery=self).order_by('like', 'view', 'dislike').gallery
            serializer = GallerySerializer(instance=obj, many=True)
        else:
            serializer = GallerySerializer(instance=Gallery.objects.all(), many=True)
        return Response(serializer.data)


class GalleryRequestView(APIView):
    def post(self, request: object) -> Response:
        serializer = GallerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
