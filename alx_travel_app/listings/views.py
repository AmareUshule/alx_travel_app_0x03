from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_email


class ListingViewSet(ModelViewSet):
    """
    API endpoint for managing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(ModelViewSet):
    """
    API endpoint for managing bookings and sending email asynchronously.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        # Trigger email asynchronously using Celery
        send_booking_email.delay(booking.id, booking.customer.email)

