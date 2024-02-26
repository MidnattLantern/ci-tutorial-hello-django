from django.shortcuts import render
from .models import Item


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

# showing only done items
def home(request):
    items = Item.objects.filter(done=True)
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
