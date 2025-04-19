from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todolist
# Create your views here.
def index(request):
    return render(request,'index.html')



# contact_us
def contact_us(request):
    return HttpResponse("This is contact page")
# about_us
def home(request):
        
    person = [
    {"name": "Alice", "age": 15},
    {"name": "Bob", "age": 34},
    {"name": "Charlie", "age": 2},
    {"name": "Diana", "age": 30},
    {"name": "Ethan", "age": 50}
    ]
    context = {
        "name":"Home page",
        "age" : "19",
        "person": person
        
        
    }
    return render(request,'home.html', context)

def list(request):
    obj = Todolist.objects.all()
    task = obj.all()
    all = obj.all().count()
    completed = obj.filter(is_completed = True).count()
    not_completed = obj.filter(is_completed = False).count()
    context = {
        "task": task,
        "all": all,
        "completed" : completed,
        "not_comple" : not_completed
    }
    return render(request,'task.html',context)

def create(request):
    if request.method == "post":
        title = request.post('title')
        description = request.POST.get('description')
        if title == ''and description == '':
            context = {
                "error":"Both fields are required."
            }
            return render(request,'create.html', context)
        
        Todolist.objects.create(title = title, description = description)
        return redirect('/task/')
        
    return render(request,'create.html')

def mark(request, pk):
    task = Todolist.objects.get(pk = pk)
    task.is_completed = True
    task.save()
    return redirect ('/task')

def edit(request,pk):
    task = Todolist.objects.get(pk = pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/task')
    context = {
        "task" : task
    }
    
    return render (request, 'edit.html', context)

def delete(request,pk):
    task = Todolist.objects.get(pk = pk)
    task.save()
    return redirect('/task')


