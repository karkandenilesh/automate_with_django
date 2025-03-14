import csv
from django.core.management.base import BaseCommand
from django.apps import apps
import datetime


# Proposed Command = python manage.py exportdata model_name

class Command(BaseCommand):
    help = "Export data from the database to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='model name')


    def handle(self, *args, **kwargs):

        model_name = kwargs['model_name'].capitalize()

        print(model_name)

        #search through all the installed apps for the model
        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass

        if not model:
            self.stderr.write(f'Model {model_name} not found.')
            return
        # fetch data from the database
        data = model.objects.all()

        # generate a timestamp of current data and time
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


        # define the csv file path

        file_path = f'exported_{model_name}_data_{timestamp}.csv'
        print(file_path)


        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)


            #Write the CSV header
            writer.writerow([field.name for field in model._meta.fields])

            # write the data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))