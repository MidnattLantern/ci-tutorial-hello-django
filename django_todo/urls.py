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
from todo import views
from goatapp.views import say_goaty, say_goaty2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete'),

    path('goaty/', say_goaty, name='goaty'),
    path('home/', views.home, name='home'),
    path('goaty2/', say_goaty2, name='goaty2'),

    path('only_done/', views.only_done, name='only_done'),
    path('only_undone/', views.only_undone, name='only_undone'),
]
