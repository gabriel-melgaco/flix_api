import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo a ser importado'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get('name')
                birthday = datetime.strptime(row.get('birthday'), '%Y-%m-%d').date()
                nationality = row.get('nationality')

                self.stdout.write(self.style.NOTICE(f'Importing actor: {name}'))
                
                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )
        self.stdout.write(self.style.SUCCESS(f'Actors imported from {file_name} successfully.'))
