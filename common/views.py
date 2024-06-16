from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import FileResponse
from .models import Image
from django.core.files.storage import default_storage
import magic
import os
import uuid

# Create your views here.
class ImageView(APIView):
    valid_image_extension = ['.jpg', '.jpeg', '.png', '.svg', '.gif']
    valid_image_content = ['image/jpg', 'image/jpeg',  'image/png', 'image/svg+xml', 'image/gif']

    def get(self, request: object, pk: str = None) -> Response:
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not default_storage.exists(pk):
            return Response(status=status.HTTP_403_FORBIDDEN)

        image = default_storage.open(pk)
        mimetype = magic.from_file(str(image), mime=True)
        return FileResponse(image, content_type=mimetype)


    def post(self, request: object) -> Response:
        image = request.FILES.get('image')
        if not image:
            return Response({'msg':'Image not found'}, status=status.HTTP_400_BAD_REQUEST)

        name, extension = os.path.splitext(image.name)

        if extension.lower() not in self.valid_image_extension:
            return Response({'msg':'Invalid extension'}, status=status.HTTP_400_BAD_REQUEST)

        if image.content_type not in self.valid_image_content:
            return Response({'msg':'Invalid image'}, status=status.HTTP_400_BAD_REQUEST)

        if image.size > 5 * 1024 * 1024:
            return Response({'msg':'Image too large'}, status=status.HTTP_400_BAD_REQUEST)

        filename = f'{uuid.uuid4()}{extension}'

        try:
            path = default_storage.save(filename, image)
            Image.objects.create(url=path)
            return Response({'url':path}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)