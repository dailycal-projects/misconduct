import os
import copytext
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from misconduct.models import Case
from django.core.files import File


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        Case.objects.all().delete()
        path = os.path.join(settings.DATA_DIR, 'uc_misconduct.xlsx')
        copy = copytext.Copy(path)
        for row in copy['complaints']:
            case = Case(
                campus = row['campus'],
                respondent = row['respondent'],
                respondent_position = row['respondent_position'],
                description = row['description'],
                resolution = row['resolution'],
                staff_or_student = row['staff_or_student'].upper(),
            )
            if row['complaint_date']:
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