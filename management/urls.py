from django.urls import path
from management.views import hello

urlpatterns = [
    path("hello/", hello),
]
