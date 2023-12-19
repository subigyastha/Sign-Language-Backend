from rest_framework import serializers
from .models import Dictionary,SignVideo


class dictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model= Dictionary
        fields= '__all__'

class dictionaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dictionary
        fields= ['name','id']



class SignVideoSerializer(serializers.ModelSerializer):
    dictionary_name = serializers.CharField(source='dictionary_name.name', read_only=True)

    class Meta:
        model = SignVideo
        fields = '__all__'


class SignVideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignVideo
        fields = ['dictionary_name', 'video_file',]

