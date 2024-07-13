# from django.shortcuts import render

# # Create your views here.
# # views.py
# from rest_framework import generics, permissions
# from .models import Interest, ChatMessage
# from .serializers import InterestSerializer, ChatMessageSerializer

# class InterestListCreateView(generics.ListCreateAPIView):
#     queryset = Interest.objects.all()
#     serializer_class = InterestSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class InterestUpdateView(generics.UpdateAPIView):
#     queryset = Interest.objects.all()
#     serializer_class = InterestSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class ChatMessageListCreateView(generics.ListCreateAPIView):
#     queryset = ChatMessage.objects.all()
#     serializer_class = ChatMessageSerializer
#     permission_classes = [permissions.IsAuthenticated]
# views.py
from rest_framework import generics, permissions
from .models import Interest, ChatMessage
from .serializers import InterestSerializer, ChatMessageSerializer

class InterestListCreateView(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [permissions.IsAuthenticated]

class InterestUpdateView(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
