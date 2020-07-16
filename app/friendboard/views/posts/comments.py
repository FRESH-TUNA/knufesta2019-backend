from base.views import BaseController
from friendboard.models import Comment
from friendboard.serializers.posts.comments import CommentsSerializer
from rest_framework.response import Response
import logging

class CommentsController(BaseController):
    serializer_class = CommentsSerializer
    queryset = Post.objects.all()
