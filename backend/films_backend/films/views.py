from django.shortcuts import render
from rest_framework import generics
from films.serializers import FilmSerializer
from films.models import Film

# Create your views here.
class FilmListAPIView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetailAPIView(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer