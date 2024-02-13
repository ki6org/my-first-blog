from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task


# Create your models here.
