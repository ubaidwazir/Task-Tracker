from django.shortcuts import render, redirect
from .models import TaskAssignment, TaskChoices, Task
from django.contrib.auth.models import User


def single_tasks_list_page(request, status):
    user = User.objects.filter(username="admin").first()

    if status in TaskChoices.values:
        user_tasks = TaskAssignment.objects.filter(user=user, task__status=status).select_related("task").order_by("task__due_date")
    else:
        return redirect("web:home")

    context = {
        "user_tasks":user_tasks,
        "status": status,
        "status_label": TaskChoices(status).label,
    }
    return render(request, "project/single_tasks_page.html", context)


def task_detail_page(request, id):
    task = Task.objects.get(id=id)
    task_assigned_to = task.assignments.all().select_related("user")

    context = {
        "task":task,
        "task_assigned_to":task_assigned_to,
    }
    return render(request, "project/task_detail.html", context)