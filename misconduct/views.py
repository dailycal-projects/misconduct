import os
import copytext
from django.shortcuts import render
from django.conf import settings
from bakery.views import BuildableTemplateView, BuildableListView, BuildableDetailView
from misconduct.models import Case


class CaseListView(BuildableListView):
    """
    A list of all sexual misconduct cases.
    """
    model = Case
    build_path = 'misconduct/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CaseListView, self).get_context_data(**kwargs)

        context['earliest'] = self.object_list.exclude(complaint_date=None).earliest('complaint_date').complaint_date

        return context

class CaseDetailView(BuildableDetailView):
    """
    More details about a particular sexual
    misconduct case.
    """
    model = Case

    def get_url(self, obj):
        return '/misconduct/case/' + obj.slug


class StoryView(BuildableTemplateView):

    template_name = 'misconduct/stories.html'
    build_path = 'misconduct/stories/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(StoryView, self).get_context_data(**kwargs)

        path = os.path.join(settings.DATA_DIR, 'uc_misconduct.xlsx')
        copy = copytext.Copy(path)
        context['stories'] = copy['stories']

        print(context['stories'])

        return context



class AboutView(BuildableTemplateView):
    """
    About page.
    """
    template_name = 'misconduct/about.html'
    build_path = 'misconduct/about/index.html'
