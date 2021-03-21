from rest_framework import serializers, permissions
from .models import *

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['name', 'para']
        

class ParadigmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigms
        fields = ['name']

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ['name', 'language']