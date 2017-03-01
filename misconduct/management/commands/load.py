import os
import csv
import copytext
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from misconduct.models import Case
from django.core.files import File


class Command(BaseCommand):
    help = "Load case information from spreadsheet and link to PDFs."

    def handle(self, *args, **options):
        Case.objects.all().delete()
        path = os.path.join(settings.DATA_DIR, 'uc_misconduct.csv')

        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                print(row)
                # Skip blank rows
                if not row['respondent']:
                    continue
                case = Case(
                    campus = row['campus'],
                    respondent = row['respondent'],
                    respondent_position = row['respondent_position'],
                    description = row['description'],
                    resolution = row['resolution'],
                )

                if row['complaint_date'] and row['complaint_date'] != '?':
                    case.complaint_date = row['complaint_date']

                if row['is_still_employed'] == 'Y':
                    case.is_still_employed = True
                elif row['is_still_employed'] == 'N':
                    case.is_still_employed = False

                case.save()

                # Look for the PDF
                path = os.path.join(settings.REPORT_DIR, '{}.pdf'.format(case.slug))
                if os.path.exists(path):
                    with open(path, 'rb') as f:
                        case.report = File(f)
                        case.save()