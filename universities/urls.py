from django.urls import path
from .views import universities, university_create, university_detail, university_search, topUniversities, add_to_compare, remove_from_compare, all_compared_universities

urlpatterns = [
    path('universities/', universities, name='University-list-create'),
    path('comparison/', all_compared_universities, name='university-comparasing-list'),
    path('comparison/compare/', add_to_compare, name='university-comparasing'),
    path('comparison/compare/remove/', remove_from_compare, name='university-comparasing-remove'),
    path('universities/search/', university_search, name='university-search'),
    path('universities/create/', university_create, name='university-create'),
    path('universities/<str:pk>/', university_detail, name='university-detail'),
    path('top-universities/', topUniversities, name='top-universities'),
]