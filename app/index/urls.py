from django.contrib import admin
from django.urls import path, include
from .router import Router
from .views import ProgressController

router = Router(trailing_slash=False)
router.register(r'progress', ProgressController, basename='pregress')

urlpatterns = [
    path('', include(router.urls))
]
