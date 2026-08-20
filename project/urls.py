from django.urls import path
from .views import (
    single_tasks_list_page,
    task_detail_page,
    task_delete,
    create_task,
    my_tasks,
    edit_task,
)
app_name="project"
urlpatterns = [
    path("<int:pk>/detail/", task_detail_page, name="task_detail"),
    path("<int:id>/delete/", task_delete, name="delete_task"),
    path("create/", create_task, name="create_task"),
    path("<str:status>/", single_tasks_list_page, name="single_tasks_list_page"),
    path("my-tasks", my_tasks, name="my_tasks"),
    path("<int:id>/edit/", edit_task, name="edit_task"),
]