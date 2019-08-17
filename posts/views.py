from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from .models import Author, Post
from .serializers import (
    PostSerializer, 
    PostCreateSerializer,
    AuthorSerializer
)

def home(request):
    return render(request, "index.html")

def post_detail(request, pk):
    return render(request, "post_detail.html")

class AuthorDetailView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PostListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostUpdateView(UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

class PostDeleteView(DestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Post.objects.all()
