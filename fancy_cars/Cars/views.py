from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Cars
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    '''
    Read/Retrieve
    '''
    model = Cars

class PostDetailView(DetailView):
    '''
    Read/Retrieve
    '''
    model = Cars

class PostCreateView(CreateView):
    model = Cars
    fields = ["make","model","year","price","origin","color","horsepower","description","image","active"]
    success_url = reverse_lazy("CarListView")

class PostUpdateView(UpdateView):
    '''
    Update
    '''
    model = Cars
    fields = ["make","model","year","price","origin","color","horsepower","description","image","active"]
    template_name_suffix = "_update_form"

class PostDeleteView(DeleteView):
    '''
    Delete
    '''
    model = Cars
