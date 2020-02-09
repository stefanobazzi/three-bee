from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from apiario.models import Apiario


class ApiarioList(LoginRequiredMixin, generic.ListView):
    model = Apiario

    def get_queryset(self):
        return super().get_queryset().filter(apicoltori=self.request.user.apicoltore)



class ApiarioDetail(LoginRequiredMixin, generic.DetailView):
    model = Apiario

    def get_queryset(self):
        return super().get_queryset().filter(apicoltore=self.kwargs['pk'])


class ApiarioCreate(LoginRequiredMixin, generic.CreateView):
    model = Apiario
    fields = '__all__'
    template_name = 'threebee/default_form.html'
    success_url = reverse_lazy('apiari')

    def form_valid(self, form):
        self.object = form.save()
        self.request.user.apicoltore.apiari.add(self.object)
        return super().form_valid(form)


class ApiarioUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Apiario
    fields = '__all__'
    template_name = 'threebee/default_form.html'
    success_url = reverse_lazy('apiari')


class ApiarioDelete(LoginRequiredMixin, generic.DeleteView):
    model = Apiario
    success_url = reverse_lazy('apiari')
    template_name = 'threebee/default_delete.html'