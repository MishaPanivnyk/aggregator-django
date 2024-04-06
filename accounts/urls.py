from django.urls import path
from .views import user_register, user_login, user_logout, user_profile, user_update_profile, users, users_id, send_password_reset_email, reset_password

urlpatterns = [
    path('register/', user_register, name='register'),
    path('forgot-password/', send_password_reset_email, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', reset_password, name='reset_password'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/edit/', user_update_profile, name='update_profile'),
    path('users/', users, name='users'),
    path('users/<int:pk>', users_id, name='users_id'),
]   