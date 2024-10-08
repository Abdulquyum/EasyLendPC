from django.urls import path
from . import views #home page
from .views import DisplayLaptop, LaptopDetails, AddLaptop, UpdateLaptop, DeleteLaptop, UserAddLaptop, UserDisplayLaptop #Display page and addPAge

urlpatterns = [
    path('', views.home, name="home"),
    path('checkout/', views.telegram_bot_webhook, name="checkout"),
    path('display/', DisplayLaptop.as_view(), name="display"),
    path('details/<int:pk>', LaptopDetails.as_view(), name="laptop-details"), # name - link to be referenced in html file
    path('add_laptop/', AddLaptop.as_view(), name="add-laptop"),
    path('details/edit/<int:pk>/', UpdateLaptop.as_view(), name='update_laptop'),
    path('details/<int:pk>/recycle', DeleteLaptop.as_view(), name='delete_laptop'),
    path('user/lendout', UserAddLaptop.as_view(), name='userToLend'),
    path('administration/checkpc', UserDisplayLaptop.as_view(), name='admin-check-pc'),
]
