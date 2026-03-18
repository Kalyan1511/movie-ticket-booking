from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.book_slot, name='book_slot'),
    path('booked/', views.booked_slots, name='booked_slots'),
    path('unbook/<int:id>/', views.unbook_slot, name='unbook_slot'),
]