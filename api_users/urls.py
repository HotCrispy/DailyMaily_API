from django.conf.urls import url
from .views import UserViewSet


as_view = UserViewSet.as_view({
    'post': 'create',
})

urlpatterns = [
    url(r'^register/$', as_view),
]
