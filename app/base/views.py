from rest_framework.viewsets import GenericViewSet

from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin, 
    CreateModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
)

class BaseController(
    GenericViewSet, 
    ListModelMixin, 
    RetrieveModelMixin, 
    CreateModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
):
    pass
class BaseRetrieveOnlyController(
    GenericViewSet, 
    RetrieveModelMixin
):
    pass
