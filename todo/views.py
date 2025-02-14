from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm, TagForm


class CompleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("home")

class UpdateTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, "todo/task_form.html", {"form": form})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "todo/task_form.html", {"form": form})

class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect("home")


class TagCreateView(View):
    def get(self, request):
        form = TagForm()
        return render(request, "todo/tag_form.html", {"form": form})

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
        return render(request, "todo/tag_form.html", {"form": form})


class TagUpdateView(View):
    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        form = TagForm(instance=tag)
        return render(request, "todo/tag_form.html", {"form": form})

    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
        return render(request, "todo/tag_form.html", {"form": form})


class TagDeleteView(View):
    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return redirect("tag_list")



class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("-created_at")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("home")


class TagListView(ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"

