from django.urls import path
from .views import UniversityList, UniversityCreate, UniversityDetail, UniversitySearch, TopUniversityList, AddToCompareView, RemoveFromCompareView, AllComparedUniversitiesView

urlpatterns = [
    path('universities/', UniversityList.as_view(), name='University-list-create'),
    path('comparison/', AllComparedUniversitiesView.as_view(), name='university-comparasing-list'),
    path('comparison/compare/', AddToCompareView.as_view(), name='university-comparasing'),
    path('comparison/compare/remove/', RemoveFromCompareView.as_view(), name='university-comparasing-remove'),
    path('universities/search/', UniversitySearch.as_view(), name='university-search'),
    path('universities/create/', UniversityCreate.as_view(), name='university-create'),
    path('universities/<str:pk>/', UniversityDetail.as_view(), name='university-detail'),
    path('top-universities/', TopUniversityList.as_view(), name='top-universities'),
]