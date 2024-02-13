from rest_framework import viewsets
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
