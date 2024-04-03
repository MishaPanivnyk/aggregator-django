from django.urls import path
from .views import universities, university_create, university_detail, university_search, topUniversities

urlpatterns = [
    path('universities/', universities, name='University-list-create'),
    path('universities/search/', university_search, name='university-search'),
    path('universities/create/', university_create, name='university-create'),
    path('universities/<str:pk>/', university_detail, name='university-detail'),
    path('top-universities/', topUniversities, name='top-universities'),
]