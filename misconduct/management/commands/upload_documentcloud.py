import os
from django.conf import settings
from misconduct.models import Case
from documentcloud import DocumentCloud
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Upload reports to DocumentCloud, and link to cases."

    def handle(self, *args, **options):
        username = os.environ.get('DOCUMENTCLOUD_USERNAME')
        password = os.environ.get('DOCUMENTCLOUD_PASSWORD')
        client = DocumentCloud(username, password)

        # Create the project
        project, created = client.projects.get_or_create_by_title("misconduct")

        for case in Case.objects.filter(documentcloud_id=None):
            print(case.identifier)

            # Bug: when identifier changes after python manage.py load is run, app still looks for the old identifier, erring out
            path = os.path.join(settings.REPORT_DIR, '{}.pdf'.format(case.identifier))
            print(path)
            if os.path.exists(path): 
                print("uploading ", path, case.slug)
                obj = client.documents.upload(
                    path,
                    title=case.slug,
                    related_article='http://projects.dailycal.org/misconduct/',
                    access='public'
                )

                case.documentcloud_id = obj.id
                print(obj.id)
                case.save()

                project.document_list.append(obj)
                project.put()
            # For debugging if necessary: 
            # else: 
            #     print(path, " PDF doesn't exist")
        
        
