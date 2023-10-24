from rest_framework import generics, status
from .serializers import FileSerializer, FileUploadSerializer
from .models import File
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .tasks import file_processing
# Create your views here.


class FileView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser]
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            file_processing.delay(serializer.instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)


class FileAllView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer