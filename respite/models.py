import datetime
from datetime import timedelta
from django.utils import timezone
from django.db import models

MALE = 'M'
FEMALE = 'F'
sex_choices = (
	(MALE, 'Male'),
	(FEMALE, 'Female')
)

TODAY = datetime.date.today

class FAQ(models.Model):
	question_text = models.CharField(max_length=200)
	answer_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question_text

class Patient(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	initial = models.CharField(max_length=1, blank=True)
	dob = models.DateField(blank=True, null=True)
	sex = models.CharField(max_length=1, choices=sex_choices)
	
	class Meta:
		permissions = (
			("can_see_patients", "Can see patient list and visit information"),
		)

	def __str__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

	def patient_age(self):
		# TODO: calculate time delta between today's date and patient DOB
		pass

class Visit(models.Model):
	patient = models.ForeignKey(Patient)
	stay_reason = models.TextField(max_length=500)
	stay_start_date = models.DateField(("Start date"), default=TODAY)
	stay_end_date = models.DateField("End date", blank=True, null=True)
	housing_status = models.TextField(max_length=300, blank=True)
	employment_status = models.TextField(max_length=300, blank=True)
	other_notes = models.TextField(max_length=1000, blank=True)
	referrer = models.CharField(max_length=30, blank=True)
	discharge = models.CharField(max_length=20, blank=True, null=True)
	bed_number = models.IntegerField(default=0)

	class Meta:
		ordering = ['-stay_start_date']

	def __str__(self):
		return "{0} to {1}".format(self.stay_start_date, self.stay_end_date)
		
	def length_of_stay(self):
		admitted_date = self.stay_start_date

		if not self.stay_end_date:
			length = TODAY() - admitted_date
			return length.days
		else:
			length = self.stay_end_date - admitted_date
			return length.days
















