from base.models import BaseModel
from django.db import models

class Progress(BaseModel):
    percentage = models.IntegerField(default=0)
        
    def __str__ (self):
        return "Progress bar"
