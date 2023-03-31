from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import *
from django.db.models import Q
from .models import Note
from .serializers import NoteSerializer

"""
* API Views *
"""


class NoteListAndCreate(APIView):
    permission_classes = [AllowAny]

    # Pass
    def get(self, request, *args, **kwargs):
        context = {}
        q = Q(deleted=False, owner=request.user)
        # Search in detail
        if request.GET.get("search"):
            q = q & Q(title__icontains=request.GET.get("search"))
        notes = Note.objects.filter(q)
        if notes:
            context["notes"] = NoteSerializer(instance=notes, many=True).data
            status_code = HTTP_200_OK
        else:
            context["msg"] = "Notes not found :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    # Pass
    def post(self, request, *args, **kwargs):
        context = {}
        try:
            note = Note(
                title=request.data.get("title"),
                detail=request.data.get("detail"),
                owner_id=request.user.id,
            )
            note.save()
            context["note"] = NoteSerializer(instance=note, many=False).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Note Cannot be saved :("
            status_code = HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)


class NoteSingle(APIView):
    permission_classes = [AllowAny]

    # Pass
    def get(self, request, pk, *args, **kwargs):
        context = {}
        try:
            note = Note.objects.get(id=pk, deleted=False, owner=request.user)
            context["note"] = NoteSerializer(instance=note, many=False).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Couldn't find note :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    # Pass
    def delete(self, request, pk, *args, **kwargs):
        context = {}
        try:

            note = Note.objects.get(id=pk, deleted=False, owner=request.user)
            note.delete()
            context["msg"] = "Note deleted!"
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Couldn't find note :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    # Pass
    def put(self, request, pk, *args, **kwargs):
        context = {}
        try:
            note = Note.objects.get(id=pk, deleted=False, owner=request.user)
            note.title = request.data.get("title", note.title)
            note.detail = request.data.get("detail", note.detail)
            note.save()
            context["note"] = NoteSerializer(instance=note, many=False).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Couldn't find note :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)
