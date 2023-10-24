from django.shortcuts import render
from rest_framework import generics
from .serializers import FileSerializer
from .models import File
# Create your views here.


class FileView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, serializer):
        instance = serializer.save()


class FileAllView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer