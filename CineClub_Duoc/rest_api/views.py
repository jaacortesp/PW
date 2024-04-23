from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.responde import Response
from rest_framework.parsers import JSONParser
from rest_framework.authentification import TokenAuthentification
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))