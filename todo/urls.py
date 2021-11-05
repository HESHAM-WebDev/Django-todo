from django.urls import path
from .views import index, todo_list, todo_detail
urlpatterns = [
    path('', index, name='todo-index'),
    path('list', todo_list, name='todo-list'),
    path('task/<int:task_id>/<str:task_name>', todo_detail, name='todo-detail'),
]

