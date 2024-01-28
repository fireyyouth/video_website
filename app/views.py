from django.http import JsonResponse, HttpResponse
from .models import Preview
from app.serializers import PreviewSerializer
from django.contrib.postgres.search import SearchQuery
from django.contrib.auth import logout, login, authenticate

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

def login_view(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
        return JsonResponse({
            'nickname' : user.username
        })
    else:
        return HttpResponse(status=403)


def logout_view(request):
    logout(request)
    return HttpResponse(status=200)