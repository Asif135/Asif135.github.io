from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskFrom
from django.contrib import messages
from django.core.paginator import Paginator

def todolist(request):
    if request.method == "POST":
        form = TaskFrom(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ' New Task Add')
        return redirect('todolist')
    else:
        all_task = TaskList.objects.all()
        paginator = Paginator(all_task,5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)

        return render(request, 'task.html', {"all_task": all_task})

def delete_Task(request, Task_id):
    task = TaskList.objects.get(pk=Task_id)
    task.delete()
    messages.success(request, ' Task Deleted ')
    return redirect('todolist')

def edit_Task(request, Task_id):
    if request.method == "POST":
        Task = TaskList.objects.get(pk=Task_id)
        form = TaskFrom(request.POST or none, instance = Task)
        if form.is_valid():
            form.save()
        messages.success(request, ' Task Edited ')
        return redirect('todolist')
    else:

        Task_obj= TaskList.objects.get(pk=Task_id)

        return render(request, 'edit.html', {"Task_obj": Task_obj})

def Complete_Task(request, Task_id):
    task = TaskList.objects.get(pk=Task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def Pending_Task(request, Task_id):
    task = TaskList.objects.get(pk=Task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def index(request):
    return render(request, 'index.html',)

def contact(request):
    return render(request, 'contact.html',)

def about(request):
    return render(request, 'about.html',)
