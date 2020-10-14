import json


from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Json Mixin
from testapi.mixins import JsonResponseMixin

# Serialize Data
from django.core.serializers import serialize

from .models import Update

# Create your views here.
# def detail_view(request):
#     return render (request,template,{}) # resturn JSON data -> JS Object Notation
#     return HttpResponse(get_template().render({}))


def json_example_view(request):
    """
    URI -- for a REST API
    GET -- Retrieve
    """
    data = {"count": 100, "content": "Some new content"}
    # json_data = json.dumps(data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {"count": 100, "content": "Some new content"}
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {"count": 100, "content": "Some new content"}
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()  # query_set
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type="application/json")

