from django.urls import path

from . import UserCreate

urlpatterns = [
    path('create/', UserCreate.as_view()),
]
