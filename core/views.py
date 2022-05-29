from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import  LoginView

class CustomLoginView(LoginView):
    template_name = 'login/custom_login.html'
    fields = ['__all__']
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy("tasks")


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
    template_name = 'mainpage/task_form.html'
    success_url=reverse_lazy('tasks')


class  TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = "mainpage/task_delete.html"
    success_url=reverse_lazy('tasks')
