from django.db import models
from django.contrib.auth.models import User

class TaskChoices(models.TextChoices):
    PENDING = "pending", "Pending",
    IN_PROGRESS = "in_progress", "In Progress",
    COMPLETED = "completed", "Completed"

    

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TaskChoices, default=TaskChoices.PENDING)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_created"]

    

class TaskAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.task.title} - {self.user.username}"

    
    class Meta:
        ordering = ["-assigned_at"]
        constraints = [
            models.UniqueConstraint(
                fields = ["user", "task"],
                name="unique_user_task_assignment"
            )
        ]

