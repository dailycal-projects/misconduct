from django.shortcuts import render
from bakery.views import BuildableTemplateView, BuildableListView, BuildableDetailView
from misconduct.models import Case


class CaseListView(BuildableListView):
	model = Case


class CaseDetailView(BuildableDetailView):
	model = Case
