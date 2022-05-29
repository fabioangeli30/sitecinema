from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

class TaskView(ListView):
    model = Task
    template_name = "mainpage/task_list.html"
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = "mainpage/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    template_name = "mainpage/task_form.html"
    success_url=reverse_lazy('tasks')


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'mainpage/task_update.html'
    success_url=reverse_lazy('tasks')