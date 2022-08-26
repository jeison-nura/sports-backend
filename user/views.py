from rest_freamework import APIView
from rest_framework.response import Response

class holaGuebon(APIView):
    def get(self, request):
        return Response({'hola':'hola guebon'})
