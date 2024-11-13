from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.


def task_list(request):
    #handle form submission
    if request.method == 'POST':
        #loop through all tasks
        for task in Task.objects.all():
            #Check if the task was checked in the form
            task_checkbox_name = f"task_{task.id}"#Check formatting again
            if task_checkbox_name in  request.POST:
                task.completed = True
            else:
                task.completed = False
            task.save()
        
    tasks = Task.objects.all()
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

def detail_task(request,task_id):
    task = get_object_or_404(Task,id = task_id) #ASK why it has to be id= task_id

    return render(request, 'tasks/detail_task.html', {'task':task})

def delete_task(request,task_id):
    task = get_object_or_404(Task,id = task_id) #ASK why it has to be id= task_id
    if request.method == 'POST':
        task.delete()
        return redirect('task_list') 
    return render(request, 'tasks/delete_task.html', {'task': task})
   


