from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import *
from drf_yasg.utils import swagger_auto_schema

from note.models import Note
from note.serializers import NoteSerializer
from note.dto import NoteDTO