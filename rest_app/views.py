from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class indexView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = [IsAuthenticated]

    #in above commented field we ristricted a class or throught setting.py we restricted all classes .

class ParadigmsView(viewsets.ModelViewSet):
    queryset = Paradigms.objects.all()
    serializer_class = ParadigmsSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
