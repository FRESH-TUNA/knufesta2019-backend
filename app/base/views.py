from rest_framework.viewsets import GenericViewSet

from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin, 
    CreateModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
)

class ViewSet(
    GenericViewSet, 
    ListModelMixin, 
    RetrieveModelMixin, 
    CreateModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
):
    pass
