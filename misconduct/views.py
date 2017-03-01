from django.shortcuts import render
from bakery.views import BuildableTemplateView, BuildableListView, BuildableDetailView
from misconduct.models import Case


class CaseListView(BuildableListView):
	"""A list of all sexual misconduct cases."""
	model = Case


class CaseDetailView(BuildableDetailView):
	model = Case
