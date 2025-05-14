from rest_framework import serializers

from .models import *


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'surname',
        ]



class SongSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Song
        fields = "__all__"
