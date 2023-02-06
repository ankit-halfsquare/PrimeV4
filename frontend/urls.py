from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.webix),
    path('home/', views.home),
]