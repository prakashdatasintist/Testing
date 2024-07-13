# from django.urls import path
# from .views import UserListView, ProfileListView

# urlpatterns = [
#     path('', UserListView.as_view(), name='user-list'),
#     path('profiles/', ProfileListView.as_view(), name='profile-list'),
# ]
from django.urls import path
from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]
