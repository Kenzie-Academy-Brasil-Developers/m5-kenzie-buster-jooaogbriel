# Create your views here.
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from _core.pagination import CustomLimitOffsetPagination
from .models import Movie
from users.permissions import IsEmployeeOrReadOnly
from django.shortcuts import get_object_or_404


class MovieView(APIView, CustomLimitOffsetPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]
    
    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
        

    
    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        pages = self.paginate_queryset(movies, req, view=self)
        serializer = MovieSerializer(pages, many=True)

        return self.get_paginated_response(serializer.data)




class MovieDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)


        serializer = MovieSerializer(movie)

        return Response(serializer.data)
        

    def delete(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)
        
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class MovieOrderDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, req: Request,  movie_id: int) -> Response:
        serializer = MovieOrderSerializer(data=req.data)
        movie_select = Movie.objects.get(id=movie_id)

        serializer.is_valid(raise_exception=True)
        
        serializer.save(user=req.user, movie=movie_select)

        return Response(serializer.data, status.HTTP_201_CREATED)
