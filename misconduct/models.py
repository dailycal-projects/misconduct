import os
from django.db import models
from autoslug import AutoSlugField


def report_file_name(instance, filename):
    return os.path.join(instance.slug + '.pdf')

class Case(models.Model):
	"""
	An individual sexual misconduct case.
	"""
	campus = models.CharField(max_length=56)
	respondent = models.CharField(max_length=256)
	respondent_position = models.CharField(max_length=256)
	description = models.TextField()
	resolution = models.TextField()
	complaint_date = models.DateField(null=True)
	staff_or_student = models.CharField(max_length=12)
	is_still_employed = models.NullBooleanField()
	report = models.FileField(upload_to=report_file_name)

	slug = AutoSlugField(populate_from='respondent')

	class Meta:
		ordering = ['campus', 'respondent']