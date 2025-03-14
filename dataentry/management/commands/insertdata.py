from django.core.management.base import BaseCommand
from dataentry.models import Students

class Command(BaseCommand):

    help = "This command will insert data into the database"

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no': 1, 'name': 'Kapil', 'age':65},
            {'roll_no': 2, 'name': 'Sachin', 'age':51},
            {'roll_no': 3, 'name': 'Dhoni', 'age':42},
            {'roll_no': 4, 'name': 'Kohli', 'age':36},
            {'roll_no': 5, 'name': 'Ruturaj', 'age':28},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_data = Students.objects.filter(roll_no=roll_no).exists()

            if not existing_data:
                Students.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Students with roll no {roll_no} is already exist.'))
            
        self.stdout.write("Data inserted successfully..")