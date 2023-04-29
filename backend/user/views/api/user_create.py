from user.views.imports import *


class UserCreate(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserDTO)
    def post(self, request, *args, **kwargs):
        context = {}
        user = User(
            username=request.data.get('username'),
            password=make_password(request.data.get('password'))
        )
        user.save()
        context['user'] = UserSerializer(user).data
        return Response(context, status=HTTP_201_CREATED)
