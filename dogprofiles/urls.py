from django.urls import path
from dogprofiles import views

urlpatterns = [
    path('dogprofiles/', views.DogProfileList.as_view()),
    path('dogprofiles/<int:pk>/', views.DogProfileDetail.as_view())
]
