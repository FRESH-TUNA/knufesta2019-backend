from rest_framework import serializers
from friendboard.models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
