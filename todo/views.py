from django.shortcuts import render, HttpResponse, redirect
from .models import Item


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')


def home(request):
    html_content = "<h1>Hello</h1><p>This is an HTML response.</p>"
    html_content2 = "<p>Home page</p>"
    return HttpResponse(html_content + html_content2)


def only_done(request):
    items = Item.objects.filter(done=True)
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def only_undone(request):
    items = Item.objects.filter(done=False)
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)