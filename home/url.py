from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.home),
    path('hello/', views.about),
    path('hello/', views.contact)
]