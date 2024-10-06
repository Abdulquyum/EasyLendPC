from django.urls import path
from . import views #home page
from .views import DisplayLaptop, LaptopDetails #Display page

urlpatterns = [
    path('', views.home, name="home"),
    path('display/', DisplayLaptop.as_view(), name="display"),
    path('details/<int:pk>', LaptopDetails.as_view(), name="laptop-details"), # name - link to be referenced in html file
]
