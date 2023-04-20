from django.urls import path
from .views import  list_todoItems, insert_todo, delete_todo_item



urlpatterns = [
    path('list/', list_todoItems),
    path('insert_todo/', insert_todo, name="insert_todo_item"),
    path('delete/<int:todo_id>/', delete_todo_item, name="delete_todo_item")
]