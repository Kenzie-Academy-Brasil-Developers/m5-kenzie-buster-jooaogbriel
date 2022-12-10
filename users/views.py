from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, JWTSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from users.permissions import PermissionsPersonalized



class UserView(APIView):
    
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized]
    

    def get(self, request: Request, user_id: int) -> Response:
        user = User.objects.get(id=user_id)
        self.check_object_permissions(request,user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK) 

class UserLogin(TokenObtainPairView):
    serializer_class = JWTSerializer