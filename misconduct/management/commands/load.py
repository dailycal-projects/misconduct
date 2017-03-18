import os
import csv
import copytext
from xlrd import xldate_as_tuple
from datetime import datetime
from django.conf import settings
from django.utils.text import slugify
from misconduct.models import Case
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load case information from spreadsheet and link to PDFs."

    def handle(self, *args, **options):
        # Open the data file
        path = os.path.join(settings.DATA_DIR, 'uc_misconduct.xlsx')
        copy = copytext.Copy(path)

        for row in copy['complaints']:
            # Excel date format sucks
            try:
                complaint_date = datetime(*xldate_as_tuple(float(row['complaint_date']), 0))
            except:
                complaint_date = None

            # Identifier is unique
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
                    row['id']
                )
            )

            if row['respondent_position'] and row['respondent_position'] != '?':
                case.respondent_position = row['respondent_position']

            case.save()
                    