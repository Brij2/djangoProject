from django.shortcuts import render
from django import forms

tasks = ["foo", "bar", "baz"] 

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label = "priority" , min_value = 1 , max_value = 5,)


def index(request,): 
    return render(request, "tasks/index.html", {
        "tasks": tasks
    } )

def add(request):
    if request.method == "post":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else : 
            return render(request,"tasks/add.html", {
                    "form" : form
                })

    return render(request, "tasks/add.html",{
        "form": NewTaskForm() 
    })