import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class DemoApp(APIView):
    def get(self, request):
        data = {"message": "Hello World FROM version 2"}
        return HttpResponse(json.dumps(data), content_type="application/json")
