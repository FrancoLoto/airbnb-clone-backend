from django.urls import path

from .views import (BookingListCreateView, BookingRetrieveUpdateDestroyView,
                    PropertyListCreateView, PropertyRetrieveUpdateDestroyView)

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view()),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroyView.as_view()),
    path('bookings/', BookingListCreateView.as_view()),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyView.as_view()),
]
