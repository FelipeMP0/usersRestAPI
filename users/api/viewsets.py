from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..api.serializers import UserSerializer
from ..models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'name',
        'RG',
        'CPF',
        'phoneNumber',
        'dateOfBirth',
        'address__line1',
        'address__city',
        'address__state',
        'professionalInformation__profession',
        'professionalInformation__companyName',
        'professionalInformation__position'
    )

    def get_queryset(self):
        queryset = User.objects.filter(active=True)
        return queryset

    def destroy(self, request, *args, **kwargs):
        try:
            queryset = User.objects.filter(pk=kwargs['pk'])
            user = queryset.get(pk=kwargs['pk'])
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        if user.active:
            queryset.update(RG=user.RG + 'd', CPF=user.CPF + 'd', active=False)
            return Response(status=204)
        else:
            return Response({"detail": "Not found."}, status=404)

    def retrieve(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs['pk'])
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        if user.active:
            return Response(user.to_dict())
        else:
            return Response({"detail": "Not found."}, status=404)
