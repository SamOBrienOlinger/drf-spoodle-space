from django.urls import path
from DogDanger import views

urlpatterns = [
    path('dogdanger/', views.dogDangerList.as_view()),
    path('dogdanger/<int:pk>/', views.dogDangerDetail.as_view()),
]
