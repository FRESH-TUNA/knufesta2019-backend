from base.views import BaseRetrieveOnlyController
from .models import Progress
from .serializers import ProgressSerializer
from rest_framework.response import Response
import logging

class ProgressController(BaseRetrieveOnlyController):
    serializer_class = ProgressSerializer

    def get_object(self):
        object = Progress.objects.first()
        if (object is None):
            object = Progress.objects.create()
        return object 
