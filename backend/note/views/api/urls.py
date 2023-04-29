from django.urls import path

from . import NoteListAndCreate, NoteSingle

urlpatterns = [
    path('', NoteListAndCreate.as_view()),
    path('<int:pk>/', NoteSingle.as_view()),
]
