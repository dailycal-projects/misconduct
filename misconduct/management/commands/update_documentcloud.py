from documentcloud import DocumentCloud
from misconduct.models import Case
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Link cases to DocumentCloud."

    def handle(self, *args, **options):
        client = DocumentCloud()
        for case in Case.objects.filter(campus='Santa Cruz'):
            print(case.identifier)
            obj_list = client.documents.search('project:misconduct title:' + case.identifier)
            case.documentcloud_id = obj_list[0].id
            case.save()