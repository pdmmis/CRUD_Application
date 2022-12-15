
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home),
    path("lgn",views.login),
    path("updt",views.update),
    path("welcome",views.welcome),
    path("table",views.table),



]
