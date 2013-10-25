from django.http import HttpResponse
from api.models import Item

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def read(request, item_name):
    item = Item.objects.get(name=item_name)
    return HttpResponse("Found item: {0!r}".format(item))
