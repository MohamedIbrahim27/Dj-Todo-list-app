from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView ,DetailView ,CreateView,UpdateView ,DeleteView,FormView
from.models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Login(LoginView):
    template_name='login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('todo_list:task_list')
    
class Regiser(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('todo_list:task_list')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Regiser,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo_list:task_list')
        return super(Regiser,self).get(*args, **kwargs)
    
    
# @login_required(login_url='/todo_list/login')
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    template_name='task_list.html'
    context_object_name='task_list'
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['task_list']=context['task_list'].filter(user=self.request.user)
        context['count']=context['task_list'].filter(complete=False).count()
        search=self.request.GET.get('search') or ''
        if search:
            context['task_list']=context['task_list'].filter(title__icontains=search)
        return context
    
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    template_name='task_detail.html'
    context_object_name='task_detail'
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']
    template_name='task_form.html'
    # context_object_name='task_detail'
    success_url=reverse_lazy('todo_list:task_list')
    def form_valid(self, form):
        form.instance.user =self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    template_name='task_update.html'
    fields=['title','description','complete']
    success_url=reverse_lazy('todo_list:task_list')
    
    # context_object_name='task_update'
    
# class TaskDelete(LoginRequiredMixin,DeleteView):
#     model=Task
#     template_name='task_delete.html'
#     # fields='__all__'
#     success_url=reverse_lazy('todo_list:task_list')
    
#     context_object_name='task_delete'


def TaskDelete(request,pk):
    task_delete= Task.objects.get(pk=pk)
    task_delete.delete()
    return redirect('todo_list:task_list')