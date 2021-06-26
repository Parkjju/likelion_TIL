# tasks/views.py
from django.forms.widgets import CheckboxInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') 

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def deleteTask(request, id):
    item = Task.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def edit(request,id):
    editTodo = Task.objects.get(id=id)
    return render(request, 'tasks/edit.html',{'todo':editTodo})

def update(request, id):
    tasks = Task.objects.get(id=id)

    if request.method == "POST":
        tasks.title = request.POST.get('title')
        tasks.complete = bool(request.POST.get('complete'))
        tasks.created = timezone.now()
        tasks.save()
        return redirect('edit',tasks.id)
    return render(request, 'tasks/edit.html',{'todo':tasks})

