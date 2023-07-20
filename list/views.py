from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.models import Tag, Task


def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }

    return render(request=request, template_name="list/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    template_name = "list/task_list.html"
    context_object_name = "task_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:literary-format-list")
    template_name = "list/task_confirm_delete.html"
