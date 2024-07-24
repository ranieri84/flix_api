import csv
from datetime import datetime
from typing import Any
from django.core.management.base import BaseCommand
from actors.models import Actor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
         'file_name',
         type=str,
         help='Nome do Arquivo com Atores'
        )

    def handle(self, *args: Any, **options: Any):
        file_name = options['file_name']
        
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                nationality = row['nationality']
                birthday = datetime.strptime(row['birthday'],'%Y-%m-%d').date()
                
                self.stdout.write(self.style.NOTICE(name))
                
                Actor.objects.create(
                    name=name,
                    nationality=nationality,
                    birthday=birthday,
                )
        self.stdout.write(self.style.SUCCESS('Atores Carregados com sucesso!'))