from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from home.models import Task
# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        ins = Task(taskTitle=title, taskDesc= desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def tasks(request):
    alltasks = Task.objects.all()
    for item in alltasks:
        print(item.taskDesc)
        print("hello")
    context = {'tasks': alltasks}
    return render(request, 'tasks.html', context)

def delete(request, sno):
    context = {'success': 'False'}
    if request.method == "POST":
        ins = Task.objects.get(pk=sno)
        ins.delete()
        context = {'success': 'True', 'file':'del'}
        return redirect('/tasks')


