from django.urls import path
from .views import FileView, FileAllView


urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload'),
    path('files/', FileAllView.as_view(), name='file-all'),
]
