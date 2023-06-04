from django.urls import include
from django.urls import path

app_name = "apps.core"

urlpatterns = [
    path("v1/", include("core.v1.urls", namespace="v1")),
    path("v2/", include("core.v2.urls", namespace="v2")),
]
