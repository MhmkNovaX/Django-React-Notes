from rest_framework import serializers


class UserDTO(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()