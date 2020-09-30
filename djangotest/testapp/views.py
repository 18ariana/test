from .models import People
from .serializers import PeopleAdminListSerializer, PeopleListSerializer
from rest_framework import generics, permissions
# Create your views here.


class PeopleListView(generics.ListAPIView):

    queryset = People.objects.all()
    serializer_class = PeopleListSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdminPeopleListView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleAdminListSerializer
    permission_classes = [permissions.IsAdminUser]
