from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class TaskView(ListView):
    model = Task
    template_name = "mainpage/task_list.html"
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = "mainpage/task_detail.html"
    context_object_name= "task"

