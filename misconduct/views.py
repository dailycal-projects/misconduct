from django.shortcuts import render
from bakery.views import BuildableTemplateView, BuildableListView, BuildableDetailView
from misconduct.models import Case


class CaseListView(BuildableListView):
	"""
	A list of all sexual misconduct cases.
	"""
	model = Case
	build_path = 'misconduct/index.html'


class CaseDetailView(BuildableDetailView):
	"""
	More details about a particular sexual
	misconduct case.
	"""
	model = Case

	def get_url(self, obj):
		return '/misconduct/case/' + obj.slug


class AboutView(BuildableTemplateView):
	"""
	About page.
	"""
	template_name = 'misconduct/about.html'
	build_path = 'misconduct/about/index.html'
