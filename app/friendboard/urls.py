from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.posts import PostController

router = SimpleRouter(trailing_slash=False)
router.register(r'posts', PostController, basename='posts')

urlpatterns = [
    path('', include(router.urls))
]
