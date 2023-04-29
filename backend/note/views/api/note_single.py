from note.views.imports import *


class NoteSingle(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, *args, **kwargs):
        context = {}
        try:
            note = Note.objects.get(id=pk, owner=request.user)
            context["note"] = NoteSerializer(note).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Couldn't find note :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    def delete(self, request, pk, *args, **kwargs):
        context = {}
        try:
            note = Note.objects.get(id=pk, owner=request.user)
            note.delete()
            context["msg"] = "Note deleted!"
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Couldn't find note :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=NoteDTO)
    def put(self, request, pk, *args, **kwargs):
        context = {}
        try:
            note = Note.objects.get(id=pk, owner=request.user)
            note.title = request.data.get("title", note.title)
            note.detail = request.data.get("detail", note.detail)
            note.save()
            context["note"] = NoteSerializer(note).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Couldn't find note :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)
