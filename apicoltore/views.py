from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from apicoltore.models import Apicoltore


class ApicoltoreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Apicoltore
   # template_name = 'apicoltore/apicoltore_detail.html'