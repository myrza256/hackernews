from django.urls import path
from knox import views as knox_views

from users.views import UserListView, RegisterView, LoginView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/register/', RegisterView.as_view()),
    path('users/login/', LoginView.as_view()),
    path('users/logout/', knox_views.LogoutView.as_view(), name='knox_logout')
]
