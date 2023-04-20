from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
def list_todoItems(request):
    context={'todo_list': Todo.objects.all()}
    return render(request, 'list/todo_list.html', context)
def insert_todo(request:HttpRequest):
    content=request.POST['content']
    todo=Todo(content=content)
    todo.save()
    return redirect('/todos/list/')
def delete_todo_item(request, todo_id):
    delete_item=Todo.objects.get(id=todo_id)
    delete_item.delete()
    return redirect('/todos/list/')





