from django.shortcuts import render
from project.models import TaskAssignment, TaskChoices
from django.contrib.auth.models import User

def home(request):
    user = User.objects.filter(username="admin").first()
    
    user_pending_tasks = TaskAssignment.objects.filter(user=user, task__status=TaskChoices.PENDING).order_by("task__due_date")[:6].select_related("task")
    user_in_progress_tasks = TaskAssignment.objects.filter(user=user, task__status=TaskChoices.IN_PROGRESS).order_by("task__due_date")[:6].select_related("task")
    user_completed_tasks = TaskAssignment.objects.filter(user=user, task__status=TaskChoices.COMPLETED).order_by("task__due_date")[:6].select_related("task")

    user_pending_tasks_count = TaskAssignment.objects.filter(user=user, task__status=TaskChoices.PENDING).count()
    user_in_progress_tasks_count = TaskAssignment.objects.filter(user=user, task__status=TaskChoices.IN_PROGRESS).count()
    user_completed_tasks_count = TaskAssignment.objects.filter(user=user, task__status=TaskChoices.COMPLETED).count()

    context = {
        "user_pending_tasks": user_pending_tasks,
        "user_in_progress_tasks": user_in_progress_tasks,
        "user_completed_tasks": user_completed_tasks,
        
        "user_pending_tasks_count": user_pending_tasks_count,
        "user_in_progress_tasks_count": user_in_progress_tasks_count,
        "user_completed_tasks_count": user_completed_tasks_count,
    }
    return render(request, "web/home.html", context)