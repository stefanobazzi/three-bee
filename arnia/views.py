from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from arnia.models import Arnia


class ArniaList(LoginRequiredMixin, generic.ListView):
    model = Arnia

    def get_queryset(self):
        return super().get_queryset().filter(apiari__apicoltori=self.request.user.apicoltore)


class ArniaDetail(LoginRequiredMixin, generic.DetailView):
    model = Arnia

    def get_queryset(self):
        return super().get_queryset().filter(apiari__apicoltori=self.request.user.apicoltore)


class ArniaCreate(LoginRequiredMixin, generic.CreateView):
    model = Arnia
    fields = '__all__'
    template_name = 'threebee/default_form.html'
    success_url = reverse_lazy('arnie')

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.request.user.apicoltore.apiari.add(self.object)
    #     return super().form_valid(form)


class ArniaUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Arnia
    fields = '__all__'
    template_name = 'threebee/default_form.html'
    success_url = reverse_lazy('arnie')


class ArniaDelete(LoginRequiredMixin, generic.DeleteView):
    model = Arnia
    success_url = reverse_lazy('arnie')
    template_name = 'threebee/default_delete.html'