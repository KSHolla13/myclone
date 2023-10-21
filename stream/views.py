from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stream.models import *
from stream.serializers import *
# Create your views here.

class MoviesView(APIView):

    def get(self, request):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self,request):    
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):

    def get(self,request,pk):
        try:
            movie = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({'error':'movie not present'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movies.objects.get(pk=pk)
        serializer = MoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)