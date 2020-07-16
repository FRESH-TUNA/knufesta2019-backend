from base.views import BaseController
from friendboard.models import Post
from friendboard.serializers.posts import PostsSerializer
from friendboard.paginator import PostPaginator
from rest_framework.response import Response
import logging

class PostController(BaseController):
    serializer_class = PostsSerializer
    pagination_class = PostPaginator
    queryset = Post.objects.all()
