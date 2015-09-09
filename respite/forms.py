from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ReferralForm(forms.Form):
    referring_agency = forms.CharField()
    referring_email = forms.CharField()
    referring_phone = forms.CharField()
    patient_first_name = forms.CharField()
    patient_last_name = forms.CharField()
    patient_initial = forms.CharField()
    patient_dob = forms.CharField()
    patient_diagnosis = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(self.cleaned_data)

        subject = 'Referral from {0}'.format(self.cleaned_data['referring_agency'])

        message = "\n\n".join([
            "REFERRAL CONTACT NUMBER: {0}".format(self.cleaned_data['referring_phone']),
            "FIRST NAME: {0}".format(self.cleaned_data['patient_first_name']),
            "LAST NAME: {0}".format(self.cleaned_data['patient_last_name']),
            "INITIAL: {0}".format(self.cleaned_data['patient_initial']),
            "DOB: {0}".format(self.cleaned_data['patient_dob']),
            "DIAGNOSIS: {0}".format(self.cleaned_data['patient_diagnosis']),
        ])
        
        clean_email = self.cleaned_data['referring_email']

        send_mail(
            subject,
            message,
            clean_email,
            settings.REFERRAL_EMAIL_RECIPIENTS,
            fail_silently=False
        )
