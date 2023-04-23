from django.urls import path
from .views import NoteListAndCreate, NoteSingle

urlpatterns = [
    # APIs
    path("api/", NoteListAndCreate.as_view(), name="NoteListAndCreate"),
    path("api/<int:pk>/", NoteSingle.as_view(), name="NoteSingle"),
]
