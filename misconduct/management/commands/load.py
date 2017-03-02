import os
import csv
from datetime import datetime
from django.utils.text import slugify
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from misconduct.models import Case
from django.core.files import File


class Command(BaseCommand):
    help = "Load case information from spreadsheet and link to PDFs."

    def handle(self, *args, **options):
        # Open the data file
        path = os.path.join(settings.DATA_DIR, 'uc_misconduct.csv')

        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                # Skip blank rows
                if not row['respondent']:
                    continue

                try:
                    complaint_date = datetime.strptime(row['complaint_date'], '%Y-%m-%d')
                except:
                    complaint_date = None

                case, created = Case.objects.get_or_create(
                    identifier = row['pdf_identifier']
                )

                case.campus = row['campus']
                case.respondent = row['respondent']
                case.complaint_date = complaint_date
                case.description = row['description']

                case.slug = slugify(
                    '{}-{}-{}'.format(
                        case.campus,
                        case.respondent,
                        case.id
                    )
                )

                if row['respondent_position'] and row['respondent_position'] != '?':
                    case.respondent_position = row['respondent_position']

                case.save()

                if created:
                    # Look for the PDF
                    path = os.path.join(settings.REPORT_DIR, '{}.pdf'.format(row['pdf_identifier']))
                    if os.path.exists(path):
                        with open(path, 'rb') as f:
                            case.report = File(f)
                            case.save()