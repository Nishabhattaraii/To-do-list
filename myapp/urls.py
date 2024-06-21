from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('todo/', views.todo_list, name='todo-list'),
]
