from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brijesh", views.brijesh, name="brijesh"),
    path("<str:name>", views.greet, name ="greet"),
]