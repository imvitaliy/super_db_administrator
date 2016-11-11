from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from api.models.connection import Connection
from api.serializers.connection import ConnectionSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def Connection(requests):
    if requests.methods == "GET":
        connection = Connection.objects.all()
        serializer = ConnectionSerializer(connection)
        return JSONResponse(serializer.data)
