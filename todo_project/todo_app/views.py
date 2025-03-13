from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    context = {'todos': todos}

    return render(request, 'todo_app/todo_list.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_app/todo_detail.html', {'todo': todo})


def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', 'pending')
        due_date_str = request.POST.get('due_date')

        due_date = None
        if due_date_str:
            due_date = timezone.datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')

        todo = Todo.objects.create(
            title=title,
            description=description,
            status=status,
            due_date=due_date,
        )

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'id': todo.id, 'title': todo.title})

        return redirect('todo_list')

    return render(request, 'todo_app/todo_form.html')


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status')
        due_date_str = request.POST.get('due_date')

        if due_date_str:
            todo.due_date = timezone.datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')
        else:
            todo.due_date = None

        todo.save()
        return redirect('todo_detail', pk=todo.pk)

    return render(request, 'todo_app/todo_form.html', {'todo': todo})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.methos == 'POST':
        todo.delete()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return redirect('todo_list')

    return render(request, 'todo_app/todo_confirm_delete.html', {'todo': todo})


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])
    def by_status(self, request):
        status = request.query_params.get('status', None)
        if status:
            todos = Todo.objects.filter(status=status)
            serializer = self.get_serializer(todos, many=True)
            return Response(serializer.data)
        return Response({"error": "Status parameter is required"}, status=400)
