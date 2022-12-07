from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404


class UserView(APIView):
    
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
