from django.core.management.base import BaseCommand
from dataentry.models import Student
# I want to add some data to database using the custom command.

class Command(BaseCommand):
    help = "It will insert data to Database"

    # def add_arguments(self, parser):
    #     parser.add_argument('name' , type=str , help='Student Name')


    def handle(self, *args, **kwargs):
        # logic goes here
        # add 1 data
        dataset = [
            {'name' : "Raghav" , 'roll_no' : 17 , 'age' : 18},
            {'name' : "Muskan" , 'roll_no' : 67 , 'age' : 21},
            {'name' : "Bro" , 'roll_no' : 11 , 'age' : 22},
            {'name' : "Shiljd" , 'roll_no' : 1005 , 'age' : 22},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(name=data['name'] , roll_no=data['roll_no'] , age=data['age'])

            else:
                self.stdout.write(self.style.WARNING(f"Student with roll no {roll_no} already exists !"))
        self.stdout.write(self.style.SUCCESS('Data Inserted successffully !'))