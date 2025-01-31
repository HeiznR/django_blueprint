from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class UserAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def signup(self, request):
        name = request.data.get("name")
        password = request.data.get("password")

        if not name or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(name=name).exists():
            return Response(
                {"error": "name already taken"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(name=name, password=password)
        # login(request, user) //return session token

        return Response(
            {"message": "User registered successfully", "user": name},
            status=status.HTTP_201_CREATED,
        )


class TaskAPIViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
