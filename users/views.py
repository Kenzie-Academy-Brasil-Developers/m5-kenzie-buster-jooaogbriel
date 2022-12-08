from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsEmployeeOrReadOnlyOrOwnerAccount



class UserView(APIView):
    
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnlyOrOwnerAccount]
    

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)

        return Response(serializer.data)