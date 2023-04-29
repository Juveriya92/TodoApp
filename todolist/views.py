from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import *

# Create your views here.
def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') 


    context={'tasks':tasks,'form':form}
    return render(request,'todolist/task_list.html',context)

def CreateTask(request):
    
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/")

    context={'form':form}
    return render(request,'todolist/create_task.html',context) 

def UpdateTask(request,pk):
    
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid:
            form.save()
        return redirect("/")

    context={'form':form}
    return render(request,'todolist/update_task.html',context) 

def DeleteTask(request,pk):

    item=Task.objects.get(id=pk)
    context={'item':item}

    if request.method=="POST":
        item.delete()
        return redirect("/")

    return render(request,'todolist/delete_task.html',context)

def home(response):
    return render(response,'todolist/extended2.html',{})