from django.core.management.base import BaseCommand


# Proposed Command -> python manage.py greeting
class Command(BaseCommand):
    help = "Greeting"

    def handle(self , *args , **kwargs):
        # Write the logic
        self.stdout.write("Greetings from Priyanshu Tripathi.")