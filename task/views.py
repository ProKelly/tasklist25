from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def list_task(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request, 'task/task.html', context)

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('task:task_list')
    
    context = {
        'form':form
    }
    return render(request, 'task/create_task.html', context)

def detail_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        'task':task
    }
    return render(request, 'task/detail_task.html', context)

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    context = {
        'form': form,
    }
    return render(request, 'task/create_task.html', context)

def delete_task(request, task_id):
    task =  get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task:task_list')
    context = {'task': task}
    return render(request, 'task/delete.html', context)