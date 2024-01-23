from django.http import JsonResponse
from .models import Preview
from app.serializers import PreviewSerializer
from django.contrib.postgres.search import SearchQuery

# Create your views here.

def search(request):
    condition = {}
    keywords = request.GET.get('keywords', '')
    if keywords:
        condition['title_tsvector'] = SearchQuery(keywords)
    kind = request.GET.get('kind', '')
    if kind:
        condition['kind'] = kind

    matched_objects = Preview.objects.filter(**condition)
    serializer = PreviewSerializer(matched_objects, many=True)
    return JsonResponse(serializer.data, safe=False)
