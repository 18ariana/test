from .models import People
from .serializers import PeopleAdminListSerializer, PeopleListSerializer, ChangePasswordSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.


class PeopleListView(generics.ListAPIView):

    queryset = People.objects.all()
    serializer_class = PeopleListSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdminPeopleListView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleAdminListSerializer
    permission_classes = [permissions.IsAdminUser]


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):

        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
