from django.urls import path

from demoapp.v1.views import DemoApp

app_name = "demoapp"

urlpatterns = [
    path("demo/", DemoApp.as_view()),
]
