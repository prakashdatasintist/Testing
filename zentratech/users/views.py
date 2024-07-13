# from django.shortcuts import render

# # Create your views here.
# # views.py
# from django.contrib.auth.models import User
# from rest_framework import generics
# from .serializers import UserSerializer

# class UserListView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# from django.contrib.auth.models import User
# from rest_framework import generics
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

# class UserListView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

# views.py
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        data = [{"id": user.id, "username": user.username} for user in users]
        return Response(data)


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
