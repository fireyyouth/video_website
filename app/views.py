from django.http import JsonResponse
from .models import Preview
from app.serializers import PreviewSerializer
from django.contrib.postgres.search import SearchQuery

# Create your views here.

def all(request):
    serializer = PreviewSerializer(Preview.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

# ref: https://zhuanlan.zhihu.com/p/523233840
def search(request, keywords):
    matched_objects = Preview.objects.filter(title_tsvector=SearchQuery(keywords))
    serializer = PreviewSerializer(matched_objects, many=True)
    return JsonResponse(serializer.data, safe=False)
