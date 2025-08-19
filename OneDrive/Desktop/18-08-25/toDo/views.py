from django.shortcuts import render, redirect

# Create your views here.
from .models import Task
from django.http import JsonResponse
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def send_data(request):
    user = {"id":1,"location":"noida","course":"mern"}
    return JsonResponse(user,safe=False)