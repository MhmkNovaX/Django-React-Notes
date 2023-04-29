from note.views.imports import *


class NoteListAndCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        context = {}
        notes = Note.objects.filter(owner=request.user)
        if notes:
            context["notes"] = NoteSerializer(notes, many=True).data
            status_code = HTTP_200_OK
        else:
            context["msg"] = "Notes not found :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=NoteDTO)
    def post(self, request, *args, **kwargs):
        context = {}
        note = Note(
            title=request.data.get("title"),
            detail=request.data.get("detail"),
            owner=request.user,
        )
        note.save()
        context["note"] = NoteSerializer(note).data
        return Response(context, status=HTTP_201_CREATED)
