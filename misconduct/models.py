import os
from django.db import models


class Case(models.Model):
	"""
	An individual sexual misconduct case.
	"""
	campus = models.CharField(max_length=56)
	complaint_date = models.DateField(null=True)
	respondent = models.CharField(max_length=256)
	respondent_position = models.CharField(max_length=256)
	description = models.TextField()
	clarification = models.TextField(null=True)
	resolution = models.TextField()
	
	staff_or_student = models.CharField(max_length=12)
	is_still_employed = models.NullBooleanField()

	identifier = models.CharField(max_length=256, unique=True)
	documentcloud_id = models.CharField(
		max_length=256,
		null=True,
		blank=True
	)
	slug = models.SlugField()

	def __str__(self):
		return self.respondent

	class Meta:
		ordering = ['-complaint_date']