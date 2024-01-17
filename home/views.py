from django.shortcuts import render
from home.models import Task
# Create your views here.

def home(request):
    if request.method == "POST":
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(tasktitle = title , taskdesc = desc)
        ins.save()
    return render(request, 'home.html')


def tasks(request):
    return render(request, 'tasks.html')