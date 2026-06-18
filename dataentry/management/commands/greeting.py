from django.core.management.base import BaseCommand


# Proposed Command -> python manage.py greeting
# Proposed output -> Hi {name} , Good Morning 
class Command(BaseCommand):
    help = "Greeting the user"


    def add_arguments(self, parser):
        parser.add_argument('name', type=str , help='Specifies user name')
    

    def handle(self , *args , **kwargs):
        # Write the logic
        name = kwargs['name']
        greeting = f'Hii {name} , Good Morning' 
        self.stdout.write(self.style.SUCCESS(greeting))