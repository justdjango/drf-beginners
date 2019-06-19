from django.contrib import admin
from django.urls import path, include
from posts.views import PostView, post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/posts/', PostView.as_view(), name='post-list'),
    path('api/post-list/', post_list, name='post-list'),
    path('api/posts/<int:pk>/', post_detail, name='post-detail')
]
