from django.urls import path
from DogProfiles import views

urlpatterns = [
    path('DogProfiles/', views.DogProfileList.as_view()),
    path('DogProfiles/<int:pk>/', views.ProfileDetail.as_view())
]
