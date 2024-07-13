# """
# URL configuration for zentratech project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# # urlpatterns = [
# #     path("admin/", admin.site.urls),
# # ]
# # urls.py
# from django.urls import path
# from main.views import InterestListCreateView, InterestUpdateView, ChatMessageListCreateView

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('interests/', InterestListCreateView.as_view(), name='interest-list-create'),
#     path('interests/<int:pk>/', InterestUpdateView.as_view(), name='interest-update'),
#     path('chats/', ChatMessageListCreateView.as_view(), name='chat-list-create'),
# ]
# urls.py
# backend/zentratech/urls.py
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Zentratech API",
      default_version='v1',
      description="API description",
      terms_of_service="https://www.example.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


from django.contrib import admin
from django.urls import path, include
from django.urls import path
from users.views import UserListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Ensure this line is correct
    path('api/main/', include('main.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
