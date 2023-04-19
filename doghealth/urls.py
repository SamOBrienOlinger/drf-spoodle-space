from django.urls import path
from doghealth import views

urlpatterns = [
    path('doghealth/', views.DogHealthList.as_view()),
    path('doghealth/<int:pk>/', views.DogHealthDetail.as_view()),
]
