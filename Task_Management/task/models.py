from django.db import models
from category.models import Category


# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="tasks")


    def __str__(self) -> str:
        return self.taskTitle
