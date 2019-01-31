from django.shortcuts import render
from rest_framework import viewsets
from .models import User,Post,Comments
from .serializers import UserSerializer,PostSerializer,CommentsSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentsView(viewsets.ModelViewSet):
    queryset= Comments.objects.all()
    serializer_class = CommentsSerializer