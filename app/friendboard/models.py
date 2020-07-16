from django.db import models
from base.models import BaseModel

# Create your models here.
class Post(BaseModel):
    content = models.TextField(default='')             # 길이 제한이 없는 문자열
    password = models.CharField(max_length=50)

    class Meta:
        ordering=['-created_at']
        
    def __str__ (self):
        return self.content


class Comment(BaseModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
