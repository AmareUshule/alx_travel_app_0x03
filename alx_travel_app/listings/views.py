from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(ModelViewSet):
    """
    API endpoint for managing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(ModelViewSet):
    """
    API endpoint for managing bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

