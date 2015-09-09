from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import datetime
from datetime import timedelta
from .forms import ReferralForm
from django.views.generic.edit import FormView
from .models import FAQ, Patient, Visit

class FaqsView(generic.ListView):
    model = FAQ
    template_name = 'respite/faqs.html'
    context_object_name = 'faq_list'

    def get_faqs(self):
        return FAQ.objects

class ReferralView(FormView):
    template_name = 'respite/referral.html'
    form_class = ReferralForm
    success_url = '/referral'

    def form_valid(self, form):
        form.send_email()
        return super(ReferralView, self).form_valid(form)

class StatusView(generic.base.TemplateView):
    template_name = 'respite/status.html'
    
    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)

        MAX_MALE_BEDS = 21
        MAX_FEMALE_BEDS = 3

        visits = Visit.objects.all()
        male_bed_vacancy_flag = False
        female_bed_vacancy_flag = False
        occupied_male_beds = 0
        occupied_female_beds = 0

        for visit in visits:
            if not visit.stay_end_date:
                if visit.patient.sex == 'M':
                    occupied_male_beds += 1
                else:
                    occupied_female_beds += 1

        if occupied_male_beds < MAX_MALE_BEDS:
            male_bed_vacancy_flag = True

        if occupied_female_beds < MAX_FEMALE_BEDS:
            female_bed_vacancy_flag = True

        context['male_bed_vacancy_flag'] = male_bed_vacancy_flag
        context['female_bed_vacancy_flag'] = female_bed_vacancy_flag

        return context

class PatientsView(generic.ListView):
    model = Patient
    template_name = 'respite/patients.html'
    context_object_name = 'patient_list'

    def get_patients(self):
        return Patient.objects

class PatientDetailsView(generic.DetailView):
    model = Patient
    template_name = 'respite/details.html'  

class StatisticsView(generic.base.TemplateView):
    template_name = 'respite/statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data(**kwargs)
        
        visits = Visit.objects.all()
        ytd_totals = {}
        ytd_male = {}
        ytd_female = {}

        for visit in visits:
            visit_start_year = visit.stay_start_date.year
            visit_end_year = visit.stay_end_date.year if visit.stay_end_date else datetime.datetime.today().year

            if visit_start_year == visit_end_year:
                
                if visit_start_year in ytd_totals:
                    ytd_totals[visit_start_year] += visit.length_of_stay()
                else:
                    ytd_totals[visit_start_year] = visit.length_of_stay()

                if visit.patient.sex == 'M':
                    if visit_start_year in ytd_male:
                        ytd_male[visit_start_year] += visit.length_of_stay()
                    else:
                        ytd_male[visit_start_year] = visit.length_of_stay()

                else:
                    if visit_start_year in ytd_female:
                        ytd_female[visit_start_year] += visit.length_of_stay()
                    else:
                        ytd_female[visit_start_year] = visit.length_of_stay()

            else:
                # what happens if years are not equal
                visit_start_day = visit.stay_start_date
                visit_end_day = visit.stay_end_date or datetime.datetime.today().date()
                first_day_of_next_year = datetime.date(visit_end_day.year, 1, 1)

                first_half = (first_day_of_next_year - visit_start_day).days
                second_half = visit.length_of_stay() - first_half

                if visit_start_year in ytd_totals:
                    ytd_totals[visit_start_year] += first_half
                else:
                    ytd_totals[visit_start_year] = first_half

                if visit_end_year in ytd_totals:
                    ytd_totals[visit_end_year] += second_half
                else:
                    ytd_totals[visit_end_year] = second_half


                if visit.patient.sex == 'M':
                    if visit_start_year in ytd_male:
                        ytd_male[visit_start_year] += first_half
                    else:
                        ytd_male[visit_start_year] = first_half

                    if visit_end_year in ytd_male:
                        ytd_male[visit_end_year] += second_half
                    else:
                        ytd_male[visit_end_year] = second_half

                else:
                    if visit_start_year in ytd_female:
                        ytd_female[visit_start_year] += first_half
                    else:
                        ytd_female[visit_start_year] = first_half

                    if visit_end_year in ytd_female:
                        ytd_female[visit_end_year] += second_half
                    else:
                        ytd_female[visit_end_year] = second_half

        context['ytd_totals'] = ytd_totals
        context['ytd_male'] = ytd_male
        context['ytd_female'] = ytd_female

        return context

class HomepageView(generic.base.TemplateView):
    template_name = 'respite/homepage.html'