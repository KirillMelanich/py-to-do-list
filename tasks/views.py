
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_confirm_delete.html"
