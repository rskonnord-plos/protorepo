from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def read(request, item_name):
    return HttpResponse("Show value for: {0!r}.".format(item_name))
