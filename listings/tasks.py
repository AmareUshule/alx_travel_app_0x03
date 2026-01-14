from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(booking_id, customer_email):
    """
    Sends booking confirmation email asynchronously.
    """
    subject = f"Booking Confirmation #{booking_id}"
    message = f"Your booking with ID {booking_id} has been successfully confirmed."
    send_mail(
        subject,
        message,
        'noreply@travelapp.com',  # From email
        [customer_email],
        fail_silently=False,
    )

