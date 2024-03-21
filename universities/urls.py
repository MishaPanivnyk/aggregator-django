from django.urls import path
from .views import universities, university_create

urlpatterns = [
    path('universities/', universities, name='University-list-create'),
    path('universities/create/', university_create, name='blog-create'),
]