from rest_framework.views import APIView
from rest_framework.permissions import *
from .models import User
from rest_framework.status import *
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password

"""
* Admin Apis *
"""


class UserListAndCreate(APIView):
    permission_classes = [IsAdminUser]

    # Pass
    def get(self, request, *args, **kwargs):
        context = {}
        users = User.objects.all()
        if users:
            context["users"] = UserSerializer(instance=users, many=True).data
            status_code = HTTP_200_OK
        else:
            context["msg"] = "No users found :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    # Passed
    def post(self, request, *args, **kwargs):
        context = {}
        # try:
        user = User(
            username=request.data.get("username"),
            password=make_password(request.data.get("password")),
        )
        if request.data.get("email"):
            user.email = request.data.get("email")
        if request.data.get("first_name"):
            user.first_name = request.data.get("first_name")
        if request.data.get("last_name"):
            user.last_name = request.data.get("last_name")
        if request.data.get("is_staff"):
            user.is_staff = request.data.get("is_staff")
        if request.data.get("is_superuser"):
            user.is_superuser = request.data.get("is_superuser")
        user.save()
        context["user"] = UserSerializer(instance=user, many=False).data
        status_code = HTTP_200_OK
        # except:
        #     context["msg"] = "Cannot create user :("
        #     status_code = HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)


class UserEditAdmin(APIView):
    permission_classes = [IsAdminUser]

    # Passed
    def put(self, request, pk, *args, **kwargs):
        context = {}
        try:
            user = User.objects.get(id=pk)
            user.username = request.data.get("username", user.username)
            user.password = request.data.get(make_password("password"), user.password)
            user.email = request.data.get("email", user.email)
            user.first_name = request.data.get("first_name", user.first_name)
            user.last_name = request.data.get("last_name", user.last_name)
            user.is_superuser = request.data.get("is_superuser", user.is_superuser)
            user.is_staff = request.data.get("is_staff", user.is_staff)
            user.save()
            context["user"] = UserSerializer(user, many=False).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "User not found :("
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    # Passed
    def delete(self, request, pk, *args, **kwargs):
        context = {}
        try:
            user = User.objects.get(id=pk)
            user.delete()
            context["msg"] = "User deleted!"
            status_code = HTTP_200_OK
        except:
            context["msg"] = "User not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)


"""
* Apis *
"""


class UserCreateAnonymous(APIView):
    permission_classes = [AllowAny]

    # Passed
    def post(self, request, *args, **kwargs):
        context = {}
        try:
            user = User(
                username=request.data.get("username"),
                password=make_password(request.data.get("password")),
            )
            if request.data.get("email"):
                user.email = request.data.get("email")
            if request.data.get("first_name"):
                user.first_name = request.data.get("first_name")
            if request.data.get("last_name"):
                user.last_name = request.data.get("last_name")
            user.save()
            context["user"] = UserSerializer(instance=user, many=False).data
            status_code = HTTP_200_OK
        except:
            context["msg"] = "Cannot create user :("
            status_code = HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)


class UserEditLoggedIn(APIView):
    permission_classes = [IsAuthenticated]

    # Passed
    def put(self, request, *args, **kwargs):
        context = {}
        user = User.objects.get(id=request.user.id)
        user.username = request.data.get("username", user.username)
        user.password = request.data.get(make_password("password"), user.password)
        user.email = request.data.get("email", user.email)
        user.first_name = request.data.get("first_name", user.first_name)
        user.last_name = request.data.get("last_name", user.last_name)
        user.save()
        context["user"] = UserSerializer(user, many=False).data
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    # Passed
    def get(self, request, *args, **kwargs):
        context = {}
        user = User.objects.get(id=request.user.id)
        context["user"] = UserSerializer(user, many=False).data
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    def delete(self, request, *args, **kwargs):
        context = {}
        user = User.objects.get(id=request.user.id)
        user.delete()
        context["msg"] = "User deleted!"
        status_code = HTTP_200_OK
        return Response(context, status=status_code)