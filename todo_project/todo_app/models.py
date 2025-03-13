from django.utils import timezone
from django.db import models


# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
                        max_length=20,
                        choices=STATUS_CHOICES,
                        default="pending",
                        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_overdue(self):
        if self.due_date and self.status != 'completed':
            return timezone.now() > self.due_date
        return False
