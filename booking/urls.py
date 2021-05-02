from django.urls import path
from .views import AddAdvisor , getAdvisor, addbooking,BookDetail

urlpatterns = [
    path('<int:userid>/advisor/',getAdvisor.as_view()),
    path('<int:pk>/advisor/<int:key>/',addbooking.as_view()),
    path('<int:pk>/advisor/booking/',BookDetail.as_view())
]
 