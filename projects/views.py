from django.shortcuts import render
from projects.models import Project
from django.http import Http404
import datetime


def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        context = {"project": project}
    except Project.DoesNotExist:
        raise Http404("The Item requested does not exit")
    return render(request, "project_detail.html", context)


def bio_info(request):
    now = datetime.datetime.now()
    project = Project.objects.last()
    context = {
        'now': now,
        'project': project
    }
    return render(request, "bio_info.html", context)
