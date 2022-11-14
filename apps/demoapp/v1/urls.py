from demoapp.v1.views import DemoApp
from django.urls import path

app_name = "demoapp"

urlpatterns = [
    path("demo/", DemoApp.as_view()),
]
