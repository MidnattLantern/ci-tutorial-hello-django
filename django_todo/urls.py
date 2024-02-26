"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, add_item, edit_item
from todo.views import home, only_done, only_undone
from goatapp.views import say_goaty, say_goaty2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list'),
    path('add', add_item, name='add'),
    path('edit/<item_id>', edit_item, name='edit'),

    path('goaty/', say_goaty, name='goaty'),
    path('home/', home, name='home'),
    path('goaty2/', say_goaty2, name='goaty2'),

    path('only_done/', only_done, name='only_done'),
    path('only_undone/', only_undone, name='only_undone'),
]
