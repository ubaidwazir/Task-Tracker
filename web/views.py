from django.shortcuts import render
from project.models import Task, TaskAssignment
from django.contrib.auth.models import User

def home(request):
    user = User.objects.filter(username="admin").first()
    
    user_pending_tasks = TaskAssignment.objects.filter(user=user, task__status="pending").order_by("task__due_date")[:6]
    user_in_progress_tasks = TaskAssignment.objects.filter(user=user, task__status="in_progress").order_by("task__due_date")[:6]
    user_completed_tasks = TaskAssignment.objects.filter(user=user, task__status="completed").order_by("task__due_date")[:6]   

    context = {
        "user_pending_tasks": user_pending_tasks,
        "user_in_progress_tasks": user_in_progress_tasks,
        "user_completed_tasks": user_completed_tasks,
    }
    return render(request, "web/home.html", context)