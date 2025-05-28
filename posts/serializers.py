from .models import *
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                  'author',
                  'type',
                  'date',
                  'category',
                  'title',
                  'text',
                  'rating'
                  ]