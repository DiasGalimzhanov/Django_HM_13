from django.db import models

class Todo(models.Model):
    class TodoStatus(models.TextChoices):
        C = 'C', 'Создано'
        P = 'P', 'В процессе'
        D = 'D', 'Завершено'
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=TodoStatus.choices, default=TodoStatus.C)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
