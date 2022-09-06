from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import RegisterSerializer, UserSerializer



class RegisterUserView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(serializer.data)
        return Response({
            "user": UserSerializer(user).data,
        })

