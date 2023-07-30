from django.urls import path

from .views import hellow_view

urlpatterns = [
    path('hello/', hellow_view, name='hello'),
]
