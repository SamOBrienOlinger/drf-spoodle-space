from django.urls import path
from dogdanger import views

urlpatterns = [
    path('dogdanger/', views.DogDangerList.as_view()),
    path('dogdanger/<int:pk>/', views.DogDangerDetail.as_view()),
]
