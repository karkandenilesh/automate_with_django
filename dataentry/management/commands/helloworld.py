from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print Hello World"

    def handle(self, *args, **kwargs):
        # we write a logic inside it
        self.stdout.write("Hello World")