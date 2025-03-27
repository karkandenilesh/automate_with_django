from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student, Customer
import csv
from django.apps import apps
from django.db import DataError


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

        # get all the fields name of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        print(model_fields)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames
            if csv_header!=model_fields:
                raise DataError(f"CSV file does not match with the {model_name} table fields.")
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully'))