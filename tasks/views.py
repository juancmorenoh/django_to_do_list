from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from tasks.forms import TaskForm
from tasks.models import Task

def task_list(request):
    """
    Display and update a list of tasks.
    If the request method is POST, the view checks which tasks were marked as completed
    in the form and updates the `completed` status.
    After processing a POST request (or if the request is GET), the view retrieves all tasks 
    from the database and renders them on the 'tasks/task_list.html' template.
    
    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: The rendered 'tasks/task_list.html' template displaying all tasks, 
        with their `completed` status reflecting the latest updates.
    """
    if request.method == 'POST':
        #loop through all tasks
        for task in Task.objects.all():
            #Check if the task was checked in the form
            task_checkbox_name = f"task_{task.id}"
            if task_checkbox_name in  request.POST:
                task.completed = True
            else:
                task.completed = False
            task.save()
        
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    """
    Handles the creation of a new task.
    If the request method is POST, this view processes the submitted form to add a new task.
    If the form is valid, the new task is saved to the database, and the user is redirected 
    to the task list page. If the request method is GET, an empty form is displayed to allow
    the user to input details for a new task.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: The rendered 'tasks/add_task.html' template displaying the task creation form,
        or a redirect to the 'task_list' page if the task is successfully created.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})

def detail_task(request,task_id):
    """
    Display the details of a specific task.
    This view retrieves a single task by its ID. If the task exists, it is displayed on the 
    'tasks/detail_task.html' template. If no task with the given ID is found, a 404 error is returned.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.
        task_id (int): The ID of the task to retrieve.

    Returns:
        HttpResponse: The rendered 'tasks/detail_task.html' template displaying details of the specified task,
        or a 404 response if the task does not exist.
    """
    task = get_object_or_404(Task,id = task_id) 
    return render(request, 'tasks/detail_task.html', {'task':task})

def delete_task(request,task_id):
    """
    Handle the deletion of a specific task.
    This view retrieves a task by its ID and displays a confirmation page. If the request method is POST, 
    the task is deleted from the database, and the user is redirected to the task list page. If the 
    request method is GET, the view renders a confirmation template without deleting the task.


    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.
        task_id (int): The ID of the task to be deleted.

    Returns:
        HttpResponse: The rendered 'tasks/delete_task.html' template displaying the task and a confirmation 
        prompt, or a redirect to the 'task_list' page after the task is successfully deleted.
    """
    task = get_object_or_404(Task,id = task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list') 
    return render(request, 'tasks/delete_task.html', {'task': task})
   
def reset(request):
    """
    Delete all tasks and reset the task list.
    This view deletes all tasks from the database when the request method is POST. After deleting
    all tasks, the user is redirected to the task list page. If the request method is GET, 
    a confirmation page is displayed to ensure the user wants to proceed with the reset action.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: The rendered 'tasks/reset.html' template showing a reset confirmation prompt, 
        or a redirect to the 'task_list' page after all tasks are deleted.
    """
    if request.method == 'POST':
        Task.objects.all().delete()
        return redirect('task_list')
    return render(request, 'tasks/reset.html')
