from rest_framework import generics, status
from .serializers import FileSerializer, FileUploadSerializer
from .models import File
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
# Create your views here.


class FileView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser]
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileAllView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer