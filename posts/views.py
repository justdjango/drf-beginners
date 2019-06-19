from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        # if serializer.is_valid():
        return Response(serializer.data)