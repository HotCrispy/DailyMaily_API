# Create your views here.
from rest_framework import viewsets

from .serializers import UserSerializer
from base.models import Model_User as Model

CLIENT_ID = '<client-id>'
CLIENT_SECRET = '<client-secret>'


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'hash_key'
    permission_classes = []
    queryset = Model.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
