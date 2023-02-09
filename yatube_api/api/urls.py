from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/follow', FollowViewSet, basename='follow')
router_v1.register('v1/groups', GroupViewSet)
router_v1.register(
    'v1/posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
