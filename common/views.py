from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Image
from django.core.files.storage import default_storage
from config import settings
from config.settings import AWS_S3_INSTANCE_URL
import os
import uuid


# Create your views here.
class ImageView(APIView):
    valid_image_extension = ['.jpg', '.jpeg', '.png', '.svg', '.gif']
    valid_image_content = ['image/jpg', 'image/jpeg',  'image/png', 'image/svg+xml', 'image/gif']

    def post(self, request: object) -> Response:
        image = request.FILES.get('image')
        if not image:
            return Response({'error': 'Image not found'}, status=status.HTTP_400_BAD_REQUEST)

        name, extension = os.path.splitext(image.name)
        if extension.lower() not in self.valid_image_extension:
            return Response({'msg': 'Invalid extension'}, status=status.HTTP_400_BAD_REQUEST)

        if image.content_type not in self.valid_image_content:
            return Response({'msg': 'Invalid image'}, status=status.HTTP_400_BAD_REQUEST)

        if image.size > 5 * 1024 * 1024:
            return Response({'msg': 'Image too large'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            path = f'{uuid.uuid4()}{extension}'
            join_path = os.path.join(settings.MEDIA_ROOT, path)
            save = default_storage.save(join_path, image)
            s3path = f'https://{AWS_S3_INSTANCE_URL}/{save}'
            Image.objects.create(url=s3path)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'url': s3path}, status=status.HTTP_200_OK)
