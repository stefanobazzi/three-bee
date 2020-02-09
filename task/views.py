from django.shortcuts import render


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from task.models import Task


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task

    def get_queryset(self):
        return super().get_queryset().filter(apicoltore=self.kwargs['pk'])


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = '__all__'
    template_name = 'threebee/default_form.html'
    success_url = reverse_lazy('tasks')

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.request.user.apicoltore.apiari.add(self.object)
    #     return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'threebee/default_form.html'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'threebee/default_delete.html'