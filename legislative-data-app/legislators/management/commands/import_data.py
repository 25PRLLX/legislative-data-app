import csv
from django.core.management.base import BaseCommand
from legislators.models import Legislator, Bill, Vote

class Command(BaseCommand):
    help = 'Import legislators, bills, and votes from CSV files into the database'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.WARNING('Deleting existing data...'))
        Legislator.objects.all().delete()
        Bill.objects.all().delete()
        Vote.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Existing data deleted.'))

        self.import_legislators()
        self.import_bills()
        self.import_votes()

    def import_legislators(self):
        """Import legislators from legislators.csv"""
        with open('data/legislators.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Legislator.objects.get_or_create(
                    id=row['id'],
                    defaults={'name': row['name']}
                )
        self.stdout.write(self.style.SUCCESS('Legislators imported.'))

    def import_bills(self):
        """Import bills from bills.csv"""
        with open('data/bills.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sponsor = None
                if row['sponsor_id']:
                    try:
                        sponsor = Legislator.objects.get(id=row['sponsor_id'])
                    except Legislator.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"Sponsor with ID {row['sponsor_id']} not found. Setting sponsor to None for bill {row['title']}"))

                bill, created = Bill.objects.get_or_create(
                    id=row['id'],
                    defaults={'title': row['title'], 'sponsor': sponsor}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created bill: {bill.title}"))
                else:
                    self.stdout.write(self.style.INFO(f"Bill already exists: {bill.title}"))

    def import_votes(self):
        """Import votes and correctly map them to bills and legislators"""
        vote_id_to_bill = {}
        with open('data/votes.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vote_id_to_bill[row['id']] = row['bill_id']

        with open('data/vote_results.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                legislator = Legislator.objects.get(id=row['legislator_id'])
                bill_id = vote_id_to_bill.get(row['vote_id'])
                try:
                    bill = Bill.objects.get(id=bill_id)
                    Vote.objects.get_or_create(
                        id=row['id'],
                        defaults={
                            'legislator': legislator,
                            'bill': bill,
                            'vote_type': row['vote_type']
                        }
                    )
                except Bill.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Bill with ID {bill_id} does not exist. Skipping vote."))

        self.stdout.write(self.style.SUCCESS('Votes imported and mapped to bills and legislators.'))
