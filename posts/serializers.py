from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'custom_id',
            'category',
            'publish_date',
            'last_updated'
        )