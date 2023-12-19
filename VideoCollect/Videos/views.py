from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import dictionarySerializer,SignVideoSerializer,SignVideoUploadSerializer,dictionaryListSerializer
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Dictionary, SignVideo
# Create your views here.
def index(request):
    return render(request,'videos/index.html')

@api_view(['GET'])
def dictionaryview(request):
    dictionarys= Dictionary.objects.all()
    serializer= dictionarySerializer(dictionarys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dictionarylist(request):
    dictionarys= Dictionary.objects.all()
    serializer= dictionaryListSerializer(dictionarys, many=True)
    return Response(serializer.data)

class SignVideolist(generics.ListAPIView):
    queryset = SignVideo.objects.all()
    serializer_class = SignVideoSerializer

class SignVideoUpload(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = SignVideoUploadSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DictionaryUpdate(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = dictionarySerializer