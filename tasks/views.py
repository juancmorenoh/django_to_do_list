from django.shortcuts import render, redirect

from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm()  # Empty form for GET request

    return render(request, 'tasks/add_task.html', {'form': form})