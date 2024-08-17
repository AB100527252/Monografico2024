from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PartidoSerializer
from .models import Partido

# Create your views here.

class PartidoViewSet(viewsets.ModelViewSet):
     queryset = Partido.objects.all()
     
     serializer_class = PartidoSerializer