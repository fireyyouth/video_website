from django.http import JsonResponse
from .models import Preview
from app.serializers import PreviewSerializer
from django.contrib.postgres.search import SearchQuery

# Create your views here.

def search(request):
    keywords = request.GET.get('keywords', '')
    if keywords:
        matched_objects = Preview.objects.filter(title_tsvector=SearchQuery(keywords))
    else:
        matched_objects = Preview.objects.all()
    serializer = PreviewSerializer(matched_objects, many=True)
    return JsonResponse(serializer.data, safe=False)
