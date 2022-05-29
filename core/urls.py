from django.urls import path

from .views import TaskView,TaskDetailView,TaskCreateView,TaskUpdateView

urlpatterns = [
    path('', TaskView.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetailView.as_view(), name='task'),
    path('create-task/',TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdateView.as_view(), name='task-update'),
]