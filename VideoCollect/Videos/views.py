from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import dictionarySerializer,SignVideoSerializer,SignVideoUploadSerializer,dictionaryListSerializer
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.views import APIView
from rest_framework import generics, status

from django.db.models import Q
import os
from django.conf import settings
from moviepy.editor import VideoFileClip, concatenate_videoclips

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






class SearchAPIView(APIView):
    def get(self, request, query):
        # Split the sentence into words
        words = query.split()

        # Initialize an empty list to store video clips
        video_clips = []

        # Search for videos for each word
        for word in words:
            # Use Q objects to filter for each word and best video
            dictionary_entries = Dictionary.objects.filter(
                Q(name__icontains=word),
                best_video__isnull=False  # Ensure there's a best video associated
            )

            for entry in dictionary_entries:
                best_video = entry.best_video
                # Append the video clip to the list
                if best_video:
                    video_clips.append(VideoFileClip(best_video.video_file.path))

        # Concatenate the video clips into a single video
        final_video = concatenate_videoclips(video_clips, method="compose")

        # Set the output directory inside MEDIA_ROOT
        output_directory = os.path.join(settings.MEDIA_ROOT, 'output')
        os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists

        # Save the final video to a file inside the output directory
        output_path = os.path.join(output_directory, 'video.mp4')
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

        # Return the path to the compiled video
        return Response({'compiled_video_path': output_path})