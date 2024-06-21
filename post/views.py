from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from gallery.models import Gallery
from rest_framework.views import APIView
from rest_framework import status
from .models import Post
from .serializers import *


# Create your views here.
class PostView(APIView):
    def get(self, request: object, pk: int = None) -> Response:
        query: int = request.query_params.get('gallery')
        orderby: int = request.query_params.get('orderby')

        if pk:
            serializer = PostSerializer(instance=get_object_or_404(Post, pk=pk))
            return Response(serializer.data, status=status.HTTP_200_OK)

        if query:
            obj = get_object_or_404(Post, query=query)
        else:
            obj = get_object_or_404(Post)

        if orderby == 'latest':
            obj = obj.order_by('-date')

        elif orderby == 'fame':
            obj = obj.order_by('like', 'view', 'dislike')

        serializer = PostTitleSerializer(instance=obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: object) -> Response:
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int = None) -> Response:
        obj = get_object_or_404(Post, pk=pk)
        password = request.data.get('password')
        if not password == obj.password:
            return Response({'msg': 'Invalid password'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: object, pk: int = None) -> Response:
        obj = get_object_or_404(Post, pk=pk)
        password = request.data.get('password')
        if password == obj.password:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'msg':'Invalid password'}, status=status.HTTP_403_FORBIDDEN)
