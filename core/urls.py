from rest_framework_nested import routers

from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
post_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += post_router.urls
