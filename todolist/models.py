from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.utils import timezone

# ---------      Task List Model   --------- #
class TaskList(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task")

    class Meta:
        pass

    def __str__(self):
        return self.name


# ---------      Task Model   --------- #
class Task(models.Model):
    title = models.CharField(max_length=250)  # a varchar
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_list"
    )
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    belongs_to = models.ForeignKey(
        TaskList, on_delete=models.CASCADE, related_name="tasks"
    )

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title
