from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserUpdateProfileView, UsersView, UserDetailView, SendPasswordResetEmailView, ResetPasswordView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('forgot-password/', SendPasswordResetEmailView.as_view(), name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset_password'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserUpdateProfileView.as_view(), name='update_profile'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users_id'),
]   