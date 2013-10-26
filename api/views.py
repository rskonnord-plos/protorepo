from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.models import Item
from api.serializers import ItemSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@csrf_exempt
def read(request, item_name):
    item = Item.objects.get(name=item_name)
    serializer = ItemSerializer(item)
    return JSONResponse(serializer.data)
