from django.urls import path
from .views import (
    single_tasks_list_page,
    task_detail_page,
    task_delete,
)
app_name="project"
urlpatterns = [
    path("<str:status>/", single_tasks_list_page, name="single_tasks_list_page"),
    path("<int:id>/detail/", task_detail_page, name="task_detail"),
    path("<int:id>/delete/", task_delete, name="delete_task")
]