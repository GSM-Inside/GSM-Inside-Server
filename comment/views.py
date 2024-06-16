from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import CommentSerializer, SubCommentSerializer
from .models import Comment, SubComment


# Create your views here.
class CommentView(APIView):
    def get(self, request: object, pk: int = None) -> Response:
        if not pk:
            return Response({'error': 'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        obj = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(instance=obj, many=True)
        return Response(serializer.data)

    def post(self, request: object) -> Response:
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int) -> Response:
        if not pk:
            return Response({'error': 'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        obj = get_object_or_404(Comment, pk=pk)
        password = request.data.get('password')

        if not password == obj.password:
            return Response({'error': 'password is wrong'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: object, pk: int) -> Response:
        if not pk:
            return Response({'error': 'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        obj = get_object_or_404(Comment, pk=pk)
        password = request.data.get('password')

        if not password == obj.password:
            return Response({'error': 'password is wrong'}, status=status.HTTP_403_FORBIDDEN)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubCommentView(APIView):
    def get(self, request: object, pk: int = None) -> Response:
        if not pk:
            return Response({'error': 'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        obj = SubComment.objects.filter(id=pk)
        serializer = SubCommentSerializer(instance=obj, many=True)
        return Response(serializer.data)

    def post(self, request: object) -> Response:
        serializer = SubCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: object, pk: int = None) -> Response:
        if not pk:
            return Response({'error': 'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        obj = get_object_or_404(SubComment, pk=pk)
        password = request.data.get('password')

        if not password == obj.password:
            return Response({'error': 'password is wrong'}, status=status.HTTP_403_FORBIDDEN)
        serializer = SubCommentSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: object, pk: int) -> Response:
        if not pk:
            return Response({'error': 'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        obj = get_object_or_404(SubComment, pk=pk)
        password = request.data.get('password')

        if not password == obj.password:
            return Response({'error': 'password is wrong'}, status=status.HTTP_403_FORBIDDEN)

        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
