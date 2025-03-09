from django.core.management.base import BaseCommand

# proposed output = python manage.py greeting John
# proposed output = Hello {name}, welcome to Mahindra Finance...

class Command(BaseCommand):
    help = "greets the user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies your name')

    def handle(self, *args, **kwargs):
        fname = kwargs['name']
        greeting = f'Hi {fname}, Welcome to Mahindra Finance'
        self.stdout.write(self.style.SUCCESS(greeting))