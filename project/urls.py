from django.urls import path
from .views import (
    user_pending_tasks_list,
    user_in_progress_tasks_list,
    user_completed_tasks_list,
)
app_name="project"
urlpatterns = [
    path("pending/", user_pending_tasks_list, name="user_pending_tasks"),
    path("in-progress/", user_in_progress_tasks_list, name="user_in_progress_tasks"),
    path("completed/", user_completed_tasks_list, name="user_completed_tasks"),
]