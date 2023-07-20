from django.http import HttpResponse
from django.shortcuts import render

from list.models import Tag, Task


def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }

    return render(request=request, template_name="list/index.html", context=context)