from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

class TodoList(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'todos'

class TodoDetail(DetailView):
    model = Todo
    template_name = 'detail.html'

class TodoCreate(CreateView):
    model = Todo
    template_name = 'create.html'
    form_class = TodoForm
    success_url = reverse_lazy('home')

class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'update.html'
    form_class = TodoForm
    success_url = reverse_lazy('home')

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    



