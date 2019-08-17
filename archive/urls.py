from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet


router = DefaultRouter()

router.register('posts', PostViewSet)

post_detail = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', include(router.urls)),
    path('custom/', post_detail, name='custom')
]