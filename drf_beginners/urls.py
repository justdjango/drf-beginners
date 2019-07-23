from django.contrib import admin
from django.urls import path, include
from posts.views import (
    PostView, post_list, post_detail, PostMixinListView, PostListView,
    PostDetailView, PostDestroyView, OwnerDetailView, CommentDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/owner/<pk>/', OwnerDetailView.as_view(), name='owner-detail'),
    path('api/comment/<pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/posts/<pk>/delete/', PostDestroyView.as_view(), name='post-destroy'),
    # path('api/posts/', PostView.as_view(), name='post-list'),
    # path('api/posts/<pk>/', PostView.as_view(), name='post-detail'),
    # path('api/post-list/', post_list, name='post-list'),
    # path('api/posts/<int:pk>/', post_detail, name='post-detail')
]
