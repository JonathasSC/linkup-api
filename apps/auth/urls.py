from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterView, LoginView

urlpatterns = [
    path('token/', views.obtain_auth_token, name='token_auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
