from django.urls import path
from .views import login, register, homepage, profile, logout


urlpatterns = [
    path('', homepage, name='homepage'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout')
]
