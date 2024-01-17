from django.shortcuts import render
from home.models import Task
# Create your views here.

def home(request):
    context ={'success' : False}
    if request.method == "POST":
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(tasktitle = title , taskdesc = desc)
        ins.save()
        context ={'success' : True}
    return render(request, 'home.html', context)


def tasks(request):
    allTask = Task.objects.all()
    print(allTask)

    for item in allTask:
        print(item.taskdesc)
    context = {'tasks' : allTask}

    return render(request, 'tasks.html', context)