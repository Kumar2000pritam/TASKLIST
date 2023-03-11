from django.shortcuts import render,redirect
from .models import task

def home(request):
    tasks=task.objects.all()
    return render(request, 'home.html',{'context':tasks})

def addtask(request):
    if request.method=='POST':
        tasktitle=request.POST['TaskTitle']
        print(tasktitle)
        x=task.objects.create(title=tasktitle)
        x.save()
        return redirect('home')

    return render(request,'addtask.html')

def update(request, name):
    get_task=task.objects.get(title=name)
    if request.method=='POST':
        tasktitle=request.POST['TaskTitle']
        get_task.title=tasktitle
        get_task.save(update_fields=['title'])
        return redirect('home')
    return render(request,'update.html',{"context":get_task})



def delete(request, name):
    get_task=task.objects.get(title=name)
    get_task.delete()
    return redirect('home')
   