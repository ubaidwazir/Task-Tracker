from django.urls import path
from .views import (
    single_tasks_list_page,
)
app_name="project"
urlpatterns = [
    path("<str:status>/", single_tasks_list_page, name="single_tasks_list_page") # have to setup the regext for this path.

]