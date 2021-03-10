from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Post, Task
from . forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def homepage(request):
    return render(request, 'webpages/homepage.html')


def calorie_tracker(request):
    return render(request, 'webpages/calorie tracker.html')


def body_fat_percentage(request):
    return render(request, 'webpages/body fat percentage.html')


def to_do(request):
    task = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/to_do/')

    context = {
        'tasks': task,
        'form': form,
    }

    return render(request, 'webpages/to do.html', context)


def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/to_do/')

    context = {
        'form': form
    }

    return render(request, 'webpages/update_task.html', context)


def DeleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/to_do/')

    context = {
        'item': item,
    }

    return render(request, 'webpages/delete_task.html', context)


def body_mass_index(request):
    return render(request, 'webpages/body_mass_index.html')


def calorie_calculator(request):
    return render(request, 'webpages/calorie_calculator.html')


def forum(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'webpages/forum.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'webpages/forum.html'  # <app>/<model?_<viewtype>/html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forum/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

