from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student, Customer
import csv
from django.apps import apps


# proposed commands = python manage.py importdata filepath model_name

class Command(BaseCommand):
    help = "This command will insert students into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='File path to the csv file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):

        model = None

        # file_path = kwargs['file_path']
        file_path = kwargs.get('file_path')
        model_name = kwargs.get('model_name').capitalize()

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching the model if found.
            except LookupError:
                continue # continue searching for the model

        if not model:
            raise CommandError(f'Model {model_name} not found in any app..')



        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully'))