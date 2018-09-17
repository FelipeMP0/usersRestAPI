from rest_framework.viewsets import ModelViewSet
from ..api.serializers import UserSerializer
from ..models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(active=True)
        return queryset

