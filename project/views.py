from django.shortcuts import render
from .models import Task, TaskAssignment
from django.contrib.auth.models import User


def user_pending_tasks_list(request):
    user = User.objects.get(username="admin")

    pending_tasks = TaskAssignment.objects.filter(user=user, task__status="pending").order_by("task__due_date")

    return render(request, "project/pending_tasks.html", {"pending_tasks":pending_tasks})


def user_in_progress_tasks_list(request):
    user = User.objects.get(username="admin")

    in_progress_tasks = TaskAssignment.objects.filter(user=user, task__status="in_progress").order_by("task__due_date")

    return render(request, "project/in_progress_tasks.html", {"in_progress_tasks": in_progress_tasks})


def user_completed_tasks_list(request):
    user = User.objects.get(username="admin")

    completed_tasks = TaskAssignment.objects.filter(user=user, task__status="completed").order_by("-task__completed_at")

    return render(request, "project/completed_tasks.html", {"completed_tasks": completed_tasks})