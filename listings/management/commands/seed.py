from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # number of sample listings
            Listing.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                price=fake.random_number(digits=4),
                location=fake.city()
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))

