from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TaskAssignment, TaskChoices, Task
from django.contrib.auth.models import User
from .forms import CreateTaskForm, AssignedToForm


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


def task_detail_page(request, pk):
    task = Task.objects.get(id=pk)
    task_assigned_to = task.assignments.all().select_related("user")

    context = {
        "task":task,
        "task_assigned_to":task_assigned_to,
    }
    return render(request, "project/task_detail.html", context)


def task_delete(request, id):
    Task.objects.get(id=id).delete()
    return redirect("web:home")


def create_task(request):
    if request.method == "POST":
        task_create = CreateTaskForm(request.POST)
        if task_create.is_valid():
            task = task_create.save()
            messages.success(request, "Task created successfully!")
            return redirect(task)
    else:
        task_create = CreateTaskForm()

    return render(request, "project/task_form.html", {"task_create":task_create})


def my_tasks(request):
    user = User.objects.filter(username="admin").first()

    tasks = Task.objects.filter(owner__username="admin")

    pending_tasks = Task.objects.filter(owner__username="admin", status=TaskChoices.PENDING)
    in_progress_tasks = Task.objects.filter(owner__username="admin", status=TaskChoices.IN_PROGRESS)
    completed_tasks = Task.objects.filter(owner__username="admin", status=TaskChoices.COMPLETED)

    context = {
        "tasks":tasks,
        "pending_tasks": pending_tasks,
        "in_progress_tasks": in_progress_tasks,
        "completed_tasks": completed_tasks,
    }
    return render(request, "project/my_tasks.html", context)


def edit_task(request, id):
    task = Task.objects.get(id=id)
    
    assigned_tasks = task.assignments.select_related("user")

    if request.method == "POST":
        task_create = CreateTaskForm(request.POST, instance=task)
        assigned_to = AssignedToForm(request.POST)
        
        if "save_task" in request.POST:
            if task_create.is_valid():
                task = task_create.save()
                messages.success(request, "Task Saved Successfully!")
                return redirect(task)
        
        elif "save_assignment" in request.POST:
            if assigned_to.is_valid():
                assigned_to.save()
                messages.success(request, "Assignment Updated Successfully!")
                return redirect(task)
        
        elif "remove_assignment" in request.POST:
            user = request.POST["remove_assignment"]
            remove_user = TaskAssignment.objects.filter(user=user, task__id=id)
            remove_user.delete()
            messages.success(request, "User has been successfully removed from this task.")
            return redirect(task)

    else:
        task_create = CreateTaskForm(instance=task)
        assigned_to = AssignedToForm(instance=task)

    context = {
        "task_create":task_create,
        "assigned_to":assigned_to,
        "assigned_tasks": assigned_tasks,
    }
    
    return render(request, "project/task_form.html", context)