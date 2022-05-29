from .models import Task
from django.views.generic.list import ListView


class ModelListView(ListView):
    model = Task
    template_name = "mainpage/mainpage.html"
