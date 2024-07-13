# urls.py
from django.urls import path
from .views import InterestListCreateView, InterestUpdateView, ChatMessageListCreateView

urlpatterns = [
    path('interests/', InterestListCreateView.as_view(), name='interest-list-create'),
    path('interests/<int:pk>/', InterestUpdateView.as_view(), name='interest-update'),
    path('chats/', ChatMessageListCreateView.as_view(), name='chat-list-create'),
]
