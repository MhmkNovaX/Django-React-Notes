from rest_framework import serializers


class NoteDTO(serializers.Serializer):
    title = serializers.CharField()
    detail = serializers.CharField()
