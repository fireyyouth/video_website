from django.http import JsonResponse
from .models import Preview
from app.serializers import PreviewSerializer

# Create your views here.

def all(request):
    serializer = PreviewSerializer(Preview.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)