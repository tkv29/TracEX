from django.core.management.base import BaseCommand
from django.db import transaction
from extraction.models import PatientJourney
import csv

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the PatientJourney model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            patient_journeys = []
            for row in reader:
                patient_journey = PatientJourney(
                    name=row['name'],
                    patient_journey=row['patient_journey']
                )
                patient_journeys.append(patient_journey)
            PatientJourney.manager.bulk_create(patient_journeys)
        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))