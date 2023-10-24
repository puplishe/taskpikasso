from celery import shared_task
from .models import File
from django.core.exceptions import ObjectDoesNotExist

@shared_task()
def file_processing(file_id):
    try:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
    except ObjectDoesNotExist:
        raise Exception('File does not exist')