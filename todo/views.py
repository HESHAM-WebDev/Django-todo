from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from pprint import pprint


# Create your views here.
def index(request):

    return render(request, 'main/base_layout.html')


def todo_list(request):
    my_task_list = ['TASK-1', 'TASK-2', 'TASK-3']
    my_context = {'task_list': my_task_list, }
    return render(request, 'todo/todo_list.html', context=my_context)
    # pprint(request.META)
    # print(request.META.get('REMOTE_ADDRESS'))


def todo_detail(request, **kwargs):
    print(kwargs)
    # print(request.is_ajax())
    # print(request.is_secure())
    # print(request.GET)
    # print(request.POST)
    my_context = {
           # 'task_list': my_task_list,
            'task_id': kwargs.get('task_id'),
            'task_name': kwargs.get('task_name'),
            'task_priority': 2}

    return render(request, 'todo/todo_detail.html', context=my_context)
   #  return HttpResponse('you choosed Task Number {}'.format(kwargs))

