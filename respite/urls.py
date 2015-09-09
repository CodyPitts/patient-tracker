"""respite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(
        regex = '^$',
        view = views.HomepageView.as_view(),
        kwargs = {},
        name = 'homepage',
    ),

    url(
        '^', include('django.contrib.auth.urls')
    ),

    url(
        regex = '^faqs/$',
        view = views.FaqsView.as_view(),
        kwargs = {},
        name = 'faqs',
    ),

    url(
    	regex = '^referral/$',
    	view = views.ReferralView.as_view(),
    	kwargs = {},
    	name = 'referral',
    ),

    url(
    	regex = '^status/$',
    	view = views.StatusView.as_view(),
    	kwargs = {},
    	name = 'status',
    ),

    url(
    	regex = '^patients/$',
    	view = permission_required('respite.can_see_patients')(views.PatientsView.as_view()),
    	kwargs = {},
    	name = 'patient_list',
    ),

    url(
    	regex = '^patients/(?P<pk>[0-9]+)/$',
    	view = permission_required('respite.can_see_patients')(views.PatientDetailsView.as_view()),
    	kwargs = {},
    	name = 'patient_details',
    ),

    url(
    	regex = '^statistics/$',
    	view = views.StatisticsView.as_view(),
    	kwargs = {},
    	name = 'statistics',
    ),
]
