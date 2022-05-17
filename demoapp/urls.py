from django.urls import include
from django.urls import path

app_name = "demoapp"

urlpatterns = [
    path("v1/", include("demoapp.v1.urls", namespace="v1")),
    path("v2/", include("demoapp.v2.urls", namespace="v2")),
]
