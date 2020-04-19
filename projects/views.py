from django.shortcuts import render
from .models import Project

from .forms import CommentForm
from .models import Comment


def project_index(request):
    """
        An index view that shows a snippet of information
        about each project.
    """

    # get all project objects in the database
    projects = Project.objects.all()

    # dictionary argument for render engine
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    """
        An detail view that shows more information
        on a particular topic.

        takes a project id.
    """

    # get the project with primary key
    project = Project.objects.get(pk=pk)
    comments = Comment.objects.filter(project=project)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                project=project
            )
            comment.save()

            form = CommentForm()
            context = {
                        "project": project,
                        "comments": comments,
                        "form": form
                        }
            return render(request, 'project_detail.html', context)

        else:
            context = {
                        "project": project,
                        "comments": comments,
                        "form": form
                       }
            return render(request, 'project_detail.html', context)
    else:
        context = {
                    "project": project,
                    "comments": comments,
                    "form": form
                    }
        return render(request, 'project_detail.html', context)
